import re
from bs4 import BeautifulSoup
import requests
# from prometheus_client.decorator import getfullargspec


class DataFromNews:
    def __init__(self, filepath, link):
        self.filepath = filepath
        self.link = link

    def get_website(self):
        url = requests.get(self.link)
        news = BeautifulSoup(url.content)
        return news

    def get_data(self):
        # File html của trang web tin tức
        news = self.get_website()
        # Tiêu đề bài viết
        get_title = news.find('h1').text
        # Mô tả tóm tắt của bài viết
        get_description = news.find('p', attrs={'class': 'description'}).text
        # Nội dung bài viết
        get_detail = news.find('article', attrs={'class': 'fck_detail'})
        get_text = get_detail.findAll('p', attrs={'class': 'Normal'})
        # Dictionary lưu các nội dung
        data = {}
        data['titlte'] = get_title
        data['description'] = get_description
        text = []
        for item in get_text:
            text.append(item.text)
        data['content'] = text
        return data

    def save_data(self):
        data = self.get_data()
        file = open(self.filepath, 'a')
        file.write(data)
        file.close()


if __name__ == '__main__':
    links = 'https://vnexpress.net/de-xuat-tien-luong-tinh-dong-bao-hiem-xa-hoi-bang-70-thu-nhap-4595537.html'
    dataitem = DataFromNews(filepath='./dataset.txt', link=links)
    dataitem.save_data()