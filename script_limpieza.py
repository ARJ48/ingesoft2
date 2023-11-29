
# Importación librerías
import pandas as pd
import numpy as np
import re


def limpiar_datos(df):

    # Convertimos el campo cedula y telefono como tipo string
    try:
        df['cedula'] = df['cedula'].astype('str')

        df['telefono'] = df["telefono"].apply(lambda x: f'{x:.0f}').astype('str')
        df['telefono'] = df['telefono'].replace({'nan': np.nan})
    except:
        pass



    # # Campos de primer_nombre y primer_apellido con datos dobles
    # Separamos cuando primer_nombre o primer_apellido lleven también el segundo_nombre o segundo_apellido


    # Esta es para nombre
    try:
        df[['primer_nombre', 'segundo_nombre_temp']] = df['primer_nombre'].str.split(' ', expand=True)
        df['segundo_nombre_temp'] = df['segundo_nombre_temp'].replace({None: np.nan})
        df['segundo_nombre'] = df['segundo_nombre'].combine_first(df['segundo_nombre_temp'])
        df.drop(columns=['segundo_nombre_temp'], inplace=True)
    except:
        pass



    # Esta es para apellidos
    try:
        df[['primer_apellido', 'segundo_apellido_temp']] = df['primer_apellido'].str.split(' ', expand=True)
        df['segundo_apellido_temp'] = df['segundo_apellido_temp'].replace({None: np.nan})
        df['segundo_apellido'] = df['segundo_apellido'].combine_first(df['segundo_apellido_temp'])
        df.drop(columns=['segundo_apellido_temp'], inplace=True)
    except:
        pass



    # # Borrar duplicados
    # Unificamos los campos que sean de la misma persona y borramos duplicados

    try:
        df = df.groupby('cedula').apply(lambda group: group.ffill().bfill()).drop_duplicates('cedula').reset_index(drop=True)
    except:
        pass

    # # Validamos los tipos de cada dato
    # Validamos que por ejemplo columna cédula o teléfono no tengan caracteres, o que las columnas de nombres y apellidos tengan números


    # Definimos una función lambda que filtra los valores NaN
    filtrar_vacios = lambda x: x if pd.notna(x) else ''

    df = df.map(filtrar_vacios)

    # Definimos una función lambda que filtra los caracteres que no numéricos
    filtrar_numeros = lambda x: ''.join(filter(str.isdigit, x))

    # Definimos una función lambda que filtra los caracteres alfabéticos
    filtrar_letras = lambda x: ''.join(filter(str.isalpha, x))

    # Eliminamos caracteres de la cedula y el telefono
    # try:
    df['cedula'] = df['cedula'].map(filtrar_numeros)
    # except:
    #     pass

    try:
        df['telefono'] = df['telefono'].map(filtrar_numeros)
    except:
        pass

    # Eliminamos números de los nombres y apellidos
    try:
        df['primer_nombre'] = df['primer_nombre'].map(filtrar_letras)
    except:
        pass

    try:
        df['segundo_nombre'] = df['segundo_nombre'].map(filtrar_letras)
    except:
        pass

    try:
        df['primer_apellido'] = df['primer_apellido'].map(filtrar_letras)
    except:
        pass

    try:
        df['segundo_apellido'] = df['segundo_apellido'].map(filtrar_letras)
    except:
        pass


    df = df.replace({'': np.nan})

    # # Estandarizar direcciones
    # Se cambian algunos caracteres dentro de las direcciones para buscar su estandarización


    def estandar_direccion(address):

        try:
            address = address.lower()
            address = address.replace('#', 'no.')
            address = address.replace('cll', 'calle')
            address = address.replace('cra', 'carrera')
            address = address.replace('kra', 'carrera')
            address = address.replace('con', 'no.')
            address = address.title()

        except:
            pass

        return address

    try:
        df['direccion'] = df['direccion'].map(estandar_direccion)
    except:
        pass

    # # Validación de correo electrónico
    # Se valida a través de una expresión regular el correo electrónico, de no cumplir las normas se elimina ese valor


    def validar_correo(correo):
        patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+'
        if bool(re.match(patron, correo)):
            return correo
        else:
            return np.nan

    try:
        df['correo'] = df['correo'].map(validar_correo)
    except:
        pass

    return df
