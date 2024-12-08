# Importación de las librerías de BeautifulSoup para extracción de datos
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# Estableciento de la url de búsqueda para web scraping
url = 'https://www.homecenter.com.co/homecenter-co/category/cat70018/muebles-auxiliares-de-cocina/'

# Se crea una variable de respuesta que reciba el resultado de la petición get
respuesta = requests.get(url)

# Se genera un retraso artificialmente para esperar proceso de carga del get
time.sleep(5)

# Se crea la variable s "sopa" que recibe el texto html
s = BeautifulSoup(respuesta.text, 'html.parser')

# Se crean cuatro listas vacías que recibiran los datos a escarbar, teniendo
# en cuenta que se diferencian los precios de oferta con los precios al momento
# de hacer el scraping

Productos = [] # Nombres de productos
Precio_lista = [] # Precio de lista
Precio_hoy = [] # Precio ofertado al día 
Imagenes = [] # url de las imágenes

for link in s.find_all('h2', class_='jsx-2096706859 product-title'):
    Productos.append(link.get_text())
    
for link in s.find_all('span', class_=("jsx-3773524781 parsedPrice")):
    Precio_lista.append(link.get_text()[1:])

for i in range(0, len(Precio_lista), 2):
    Precio_hoy.append(Precio_lista[i])
        
for link in s.find_all('a', class_="jsx-71416012 link link-primary", id="testId-Link-img-pdp-link"):
    Imagenes.append(link.get('href'))

Data = pd.DataFrame()

Data['Productos'] = Productos
Data['Precios'] = Precio_hoy
Data['Imagenes'] = Imagenes

# Se exportan los datos obtenidos a un archivo csv
Data.to_csv('muebles_home_center.csv',sep=';', index=False, encoding='utf-8')




