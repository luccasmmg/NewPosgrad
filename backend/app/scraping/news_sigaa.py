#!/usr/bin/env python3
import requests
import datetime
import re
from urllib.parse import urlparse, urlunparse, quote

from bs4 import BeautifulSoup
from bs4.element import Tag
from app.schemas.base_schemas import PostGraduation
from app.schemas.scraping_schemas import NewsScraped, NewsShort

def get_news(pg: PostGraduation, skip: int, limit: int, all_news: bool):
    list_of_news = get_news_list(pg)
    limit = len(list_of_news) if all_news == True else limit
    return list(map(build_news, enumerate(list_of_news[skip:limit], start=skip)))

def get_news_short(pg: PostGraduation, skip: int, limit: int, all_news: bool):
    list_of_news = get_news_list(pg)
    limit = len(list_of_news) if all_news == True else limit
    return list(map(build_news_short, list_of_news[skip:limit]))

def get_news_list(pg: PostGraduation):
    url = f'https://sigaa.ufrn.br/sigaa/public/programa/noticias.jsf?lc=pt_BR&id={pg.id_unit}'
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser').select('#listagem li')

def build_news_short(li: Tag):
    dates = li.span.text.strip().replace('(', '').replace(')', '').split(' ')[0].split('/')
    id_news = re.findall(r'\b\d+\b', li.find('a').get('href'))[1]
    title = li.find('a').text
    return NewsShort(title=title,
                     date=datetime.date(int(dates[2]), int(dates[1]), int(dates[0])),
                     index=id_news)

def build_news(tuple_li):
    # Cant just get the link, because for some reason its broken when you select it, so we need to build it manually,
    # this will extract the id of the unit and of the news
    (index, li) = tuple_li
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
                       url=download_link,
                       index=id_news)

def build_single_news(id_unit: int, id_news: int):
    response = requests.get(f'https://sigaa.ufrn.br/sigaa/public/programa/noticias_desc.jsf?lc=pt_BR&id={id_unit}&noticia={id_news}')
    content = BeautifulSoup(response.text, 'html.parser')

    text = content.find(id='conteudo').find(class_='texto')
    download_link = "https://sigaa.ufrn.br/" + ''.join((filter(lambda i: i not in ['\n', '\t'],
                                                               content.find(class_='arquivo_baixar').a.get('href')))) if content.find(class_='arquivo_baixar') else None
    dates = content.find(id='conteudo').find(class_='data_cadastrada')
    dates.b.decompose()
    dates = dates.text.strip().replace('(', '').replace(')', '').split(' ')[0].split('/')

    return NewsScraped(title=text.h2.extract().text,
                       date=datetime.date(int(dates[2]), int(dates[1]), int(dates[0])),
                       body=text.prettify(),
                       url=download_link,
                       index=id_news)

