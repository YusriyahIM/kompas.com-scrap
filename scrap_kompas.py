from bs4 import BeautifulSoup
import requests

class BeritaKompas():

    def __init__(self):
        self.url = None
        self.article = None
        self.articles = None
    
    def open_url(self):
        """
        open indeks.kompas.com by one page only
        """
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')
        self.articles = soup.find_all("div", {"class":"article__list clearfix"})
        self.articles = list(self.articles)
        
        return self.articles

    def extract_title(self):
        """
        extract news title
        """
        if str(self.article.find("h3")) != "None":
            title = self.article.find("h3").get_text().lower()
            title = title.replace("\n", "")
            
            return title
        
    def extract_category(self):
        """
        extract news category
        """
        if str(self.article.find("div", {"class":"article__list__info"})) != "None":
            category = self.article.find("div", {"class": "article__subtitle article__subtitle--inline"}).get_text().lower()
            
            return category
        
    def extract_date_and_time(self):
        """
        extract news date and time
        """
        if str(self.article.find("div", {"class":"article__date"})) != "None":
            article_datetime = self.article.find("div", {"class": "article__date"}).get_text()
            article_datetime = article_datetime.split(',')
            extracted_date = article_datetime[0]
            extracted_time = article_datetime[1]
            
            return (extracted_date, extracted_time)

    def extract_news_url(self):
        """
        extract news URL
        """
        if str(self.article.find("h3")) != "None":
            news_url = self.article.find("a", {"class":"article__link"}).attrs['href']
            
            return news_url

    def scrap_news(self, url):
        """
        scrap indeks.kompas.com news list
        """
        self.url = url
        self.articles = self.open_url()

        news_list = []

        for self.article in self.articles:
            news_title = self.extract_title()
            news_category = self.extract_category()
            news_datetime = self.extract_date_and_time()
            news_url = self.extract_news_url()
            data = {
                'judul': news_title,
                'kategori': news_category,
                'tanggal_upload': news_datetime[0],
                'waktu_upload': news_datetime[1],
                'link_berita': news_url
            }
            news_list.append(data)
        
        return news_list
