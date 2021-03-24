#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup
from app.schemas.base_schemas import Course
from app.schemas.scraping_schemas import InstitutionalRepositoryDoc

def get_final_reports_list(course: Course, offset: int):

    url = f'{course.institutional_repository_url}?offset={offset}'

    response = requests.get(url)
    list_of_docs = BeautifulSoup(response.text, 'html.parser').select('.table tr')[1:]
    return list(map(get_final_report_details, list_of_docs))

def get_final_report_details(tr):
   response = requests.get(f"https://repositorio.ufrn.br{tr.find(headers='t2').find('a').get('href')}")
   doc = BeautifulSoup(response.text, 'html.parser')

   title=doc.find(class_='metadataFieldValue dc_title').get_text() if doc.find(class_='metadataFieldValue dc_title') else 'Não especificado'
   authors=doc.find(class_='metadataFieldValue dc_contributor_author').get_text() if doc.find(class_='metadataFieldValue dc_contributor_author') else 'Não especificado'
   keywords=doc.find(class_='metadataFieldValue dc_subject').get_text() if doc.find(class_='metadataFieldValue dc_subject') else 'Não especificado'
   issue_date=doc.find(class_='metadataFieldValue dc_date_issued').get_text() if doc.find(class_='metadataFieldValue dc_date_issued') else 'Não especificado'
   publisher=doc.find(class_='metadataFieldValue dc_publisher').get_text() if doc.find(class_='metadataFieldValue dc_publisher') else 'Não especificado'
   citation=doc.find(class_='metadataFieldValue dc_identifier_citation').get_text() if doc.find(class_='metadataFieldValue dc_identifier_citation') else 'Não especificado'
   portuguese_abstract=doc.find(class_='metadataFieldValue dc_description_resumo').get_text() if doc.find(class_='metadataFieldValue dc_description_resumo') else 'Não especificado'
   abstract=doc.find(class_='metadataFieldValue dc_description_abstract').get_text() if doc.find(class_='metadataFieldValue dc_description_abstract') else 'Não especificado'
   uri=doc.find(class_='metadataFieldValue dc_identifier_uri').find('a').get_text() if doc.find(class_='metadataFieldValue dc_identifier_uri') else 'Não especificado'

   return InstitutionalRepositoryDoc(
       title=title,
       authors=authors,
       keywords=keywords,
       issue_date=issue_date,
       publisher=publisher,
       citation=citation,
       portuguese_abstract=portuguese_abstract,
       abstract=abstract,
       uri=uri,
   )
