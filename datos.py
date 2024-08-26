from bs4 import BeautifulSoup
import pandas as pd 
import requests

#Extracción de datos de una pagina web (scraping)
url= "https://www.xataka.com/tag/ciencia-y-tecnologia"
response= requests.get(url)
bs = BeautifulSoup(response.text, "lxml")
titulos = bs.find_all("h2", class_="abstract-title")
comentarios = bs.find_all("span", class_="abstract-comment-count")
fechas = bs.find_all("time", class_="abstract-date")

# Crear el diccionario para almacenar los datos
direct_new = {'Titulos_noticias': [], 'Enlaces': [], "Comentarios": [], "Fechas": []}

# Asegurarse de que las listas tengan la misma longitud para evitar errores
for titulo, comentario, fecha in zip(titulos, comentarios, fechas):
    titulo_texto = titulo.text.strip()  # Extraer el texto del título
    enlace = titulo.a['href']  # Extraer el enlace
    comentario_texto = comentario.text.strip()  # Extraer el número de comentarios
    fecha_texto = fecha.text.strip()  # Extraer la fecha

    # Rellenar el diccionario con los datos obtenidos
    direct_new['Titulos_noticias'].append(titulo_texto)
    direct_new['Enlaces'].append(enlace)
    direct_new["Comentarios"].append(comentario_texto)
    direct_new["Fechas"].append(fecha_texto)

# Crear el DataFrame
df_news = pd.DataFrame(direct_new, columns=['Titulos_noticias', 'Enlaces', "Comentarios", "Fechas"])

print(df_news)

"""# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Juan', 'Luis', 'María'],
    'Edad': [23, 35, 29, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Acceder a una columna
edades = df['Edad']

# Filtrar el DataFrame
mayores_de_30 = df[df['Edad'] > 30]

# Mostrar los resultados
print(edades)
print(mayores_de_30)

"""