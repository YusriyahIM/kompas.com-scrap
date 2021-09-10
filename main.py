from datetime import time
from bs4 import BeautifulSoup
import json, random, re, requests
import pandas as pd
import csv   

page = str(input("Page : "))
url = "https://indeks.kompas.com/?page="+page

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data_berita = pd.DataFrame()

for p in soup.find_all("div", {"class":"article__list clearfix"}):
    #Judul
    if str(p.find("h3")) != "None":
        title = p.find("h3").get_text().lower()
        # Cleansing
        title = title.replace("\n", "")
    # kategori
    if str(p.find("div", {"class":"article__list__info"})) != "None":
        kategori = p.find("div", {"class": "article__subtitle article__subtitle--inline"}).get_text().lower()
    # Tanggal 
    if str(p.find("div", {"class":"article__date"})) != "None":
        dates = p.find("div", {"class": "article__date"}).get_text()
        dates = dates.split(',')
        date = dates[0]
    # Waktu 
    if str(p.find("div", {"class":"article__date"})) != "None":
        dates = p.find("div", {"class": "article__date"}).get_text()
        dates = dates.split(',')
        timess = dates[1]
        times = timess.replace(" WIB", "")
    # Link 
    if str(p.find("h3")) != "None":
        link = p.find("a", {"class":"article__link"}).attrs['href']
    
    data_berita = data_berita.append({'Judul': title, 'Kategori': kategori, 'Tanggal Upload': date, 'Waktu Upload': times, 'Link': link}, ignore_index=True)

print(data_berita)

data_berita.to_csv("news_kompas.csv", index=False)
print("\nData Sudah Tersimpan dengan nama : news_kompas.csv")

data_berita.to_csv('news_kompas.csv', mode='a', index=False, header=False)