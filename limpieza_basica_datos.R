
# Importación de librerías
library(tidyverse)
library(openxlsx)
library(janitor)


setwd("C:/Users/ramir/OneDrive/Escritorio/Universidad/Ingesoft 2/Proyecto/ingesoft2")


read.csv("nombres-2015.csv") %>% 
  View()

# Lectura de datos
df <- read.xlsx("bd_pruebas.xlsx") %>% 
  mutate(cedula = as.character(cedula))

df

# DEPURAMOS DUPLICADOS

df %>% 
  get_dupes(cedula)

df %>% 
  group_by(cedula) %>% 
  fill(everything(), .direction = "updown") %>% 
  fill(everything(), .direction = "downup") %>% 
  distinct(cedula, .keep_all = TRUE)

