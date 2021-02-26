import requests

from bs4 import BeautifulSoup
from bs4.element import Tag
from app.schemas.base_schemas import PostGraduation
from app.schemas.scraping_schemas import Professor

def get_professors_list(pg: PostGraduation):
    """
    Return a list of professors (dicts).
    """

    url = f"https://sigaa.ufrn.br/sigaa/public/programa/equipe.jsf?lc=pt_BR&id={pg.id_unit}"

    response = requests.get(url)
    table_lts = BeautifulSoup(response.text, 'html.parser').select('#conteudo #listagem_tabela #table_lt')
    trs = [item for sublist in [item for sublist in table_lts for item in sublist] for item in sublist if isinstance(item, Tag) and item['class'] != ['campos']]
    return list(map(create_professor, trs))

def create_professor(tr: Tag):
    tds = tr.select('td')
    lattes = tds[4].find('a').get('href') if tds[4].find('a') else 'Não encontrado'
    email = tds[5].find('a').get('href')[7:] if tds[5].find('a') else 'Não encontrado'
    professor = Professor(name=tds[0].text.strip(),
                          rank=tds[1].text.strip(),
                          level=tds[2].text.strip(),
                          phone=tds[3].text.strip(),
                          lattes=lattes,
                          email=email)
    return professor
