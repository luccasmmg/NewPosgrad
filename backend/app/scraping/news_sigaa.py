#!/usr/bin/env python3
import requests
import datetime
import re
from urllib.parse import urlparse, urlunparse, quote

from bs4 import BeautifulSoup
from bs4.element import Tag
from app.schemas.base_schemas import PostGraduation
from app.schemas.scraping_schemas import NewsScraped

def get_news_list(pg: PostGraduation, skip: int, limit: int):

    url = f'https://sigaa.ufrn.br/sigaa/public/programa/noticias.jsf?lc=pt_BR&id={pg.id_unit}'

    response = requests.get(url)
    list_of_news = BeautifulSoup(response.text, 'html.parser').select('#listagem li')
    return list(map(build_news, list_of_news[skip:limit]))

def build_news(li: Tag):
    # Cant just get the link, because for some reason its broken when you select it, so we need to build it manually,
    # this will extract the id of the unit and of the news
    numbers_in_href = re.findall(r'\b\d+\b', li.find('a').get('href'))
    id_unit, id_news  = numbers_in_href[0], numbers_in_href[1]

    response = requests.get(f'https://sigaa.ufrn.br/sigaa/public/programa/noticias_desc.jsf?lc=pt_BR&id={id_unit}&noticia={id_news}')
    content = BeautifulSoup(response.text, 'html.parser')

    text = content.find(id='conteudo').find(class_='texto')
    download_link = "https://sigaa.ufrn.br/" + ''.join((filter(lambda i: i not in ['\n', '\t'],
                                                               content.find(class_='arquivo_baixar').a.get('href')))) if content.find(class_='arquivo_baixar') else None

    dates = li.span.text.strip().replace('(', '').replace(')', '').split(' ')[0].split('/')
    return NewsScraped(title=text.h2.extract().text,
                       date=datetime.date(int(dates[2]), int(dates[1]), int(dates[0])),
                       body=text.prettify(),
                       url=download_link)
