from bs4 import BeautifulSoup 
import requests
import pandas as pd


url = "https://www.xataka.com/"
pages = ["ciencia-y-tecnologia", "elon-musk", "google", "nasa", "videojuegos"]
dict_news_03 = {"titulos_noticias": [], "enlaces": [], "comentarios": [], "fecha_publicacion": [], "tag": []}


for i in pages:
    response = requests.get(url + "tag/" + i)
    bs = BeautifulSoup(response.text,"lxml")

    temp = bs.find_all('article', "recent-abstract abstract-article")  

    for post in temp:  
        dict_news_03["titulos_noticias"].append(post.h2.a.text)
        dict_news_03["enlaces"].append(post.h2.a.get("href"))
        dict_news_03["comentarios"].append(post.span.text)
        dict_news_03["fecha_publicacion"].append(post.time.get("datetime")[0:10])
        dict_news_03["tag"].append(i)



df_news_03 = pd.DataFrame(dict_news_03, columns=["titulos_noticias", "enlaces", "comentarios", "fecha_publicacion", "tag"])
df_news_03.to_csv("./saved_data.csv", index=False)