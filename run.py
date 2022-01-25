from scrap_kompas import BeritaKompas
import pandas as pd

# initialize
kompas = BeritaKompas()
base_url = "https://indeks.kompas.com/?page="


if __name__=='__main__':

    # input maximum page count that will be extracted, start from 1
    max_page = int(input("Jumlah max.page yang akan di-scrap: "))
    
    # create empty dataframe
    df_berita = pd.DataFrame()

    for number in range(max_page):
        # create target url
        target_url = base_url + str(number+1)

        # scrap target url
        articles = kompas.scrap_news(target_url)

        # add news data into dataframe
        df_berita = df_berita.append(articles)

    # save dataframe into csv format
    df_berita.to_csv('data/kompas.csv', index=False)