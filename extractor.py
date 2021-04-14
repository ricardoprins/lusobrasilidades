import pandas as pd
import requests as r
from bs4 import BeautifulSoup


df = pd.read_csv('./brasil.csv')
string = ''
url = f'https://cidades.ibge.gov.br/brasil/{string}/historico'


def cleantxt(a: string):
    
    return a.replace("\t","").replace("\n","").strip()


def extractor(url: string):
    data = r.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    paragraphs = soup.find_all('div', {'class': 'hist__texto'})
    list = []
    for a in paragraphs:
        list.append(cleantxt(a.get_text()))
    return list
    


df.loc[:,"string"] = df.loc[:,"string"].astype(str)

#df["obs"] = extractor(df["string"])

#source.to_csv('result.csv')




