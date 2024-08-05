# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:40:28 2024

@author: usuario
"""

import pandas as pd  # Importa pandas para manipulación y análisis de datos.
from selenium import webdriver  # Importa webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importa By para localizar elementos en la página.
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para esperas explícitas.
from selenium.webdriver.support import expected_conditions as EC  # Importa condiciones esperadas para las esperas explícitas.



# Define la URL de la página principal de donde se van a extraer los datos.
PAGINA_PRINCIPAL = "https://www.scrapethissite.com/pages/simple/"

navegador = webdriver.Chrome()
navegador.get(PAGINA_PRINCIPAL)  # Abre la página web especificada por la URL.
navegador.implicitly_wait(10)

datos = []
paises= navegador.find_elements(By.CLASS_NAME, 'country')


for pais in paises:
    
    nombre = pais.find_element(By.CLASS_NAME, 'country-name')
    capital =  pais.find_element(By.CLASS_NAME, 'country-capital')
    poblacion = pais.find_element(By.CLASS_NAME, 'country-population')
    area = pais.find_element(By.CLASS_NAME, 'country-area')    
   
    datos.append({
        'NOMBRE' : nombre.text,
        'CAPITAL' : capital.text,
        'POBLACION' : poblacion.text,
        'AREA' : area.text
        })
    
                   
navegador.quit()

df = pd.DataFrame(datos)

print(df)

ruta = "C:/Users/usuario/Downloads/"

df.to_excel(ruta + "Datos proyecto.xlsx",index =False)