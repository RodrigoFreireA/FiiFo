import requests #importa a biblioteca requests
from bs4 import BeautifulSoup #importa a biblioteca beatifullSoup
import pandas as pd #importa a biblioteca Pandas

req = requests.get('https://www.clubefii.com.br/proventos-rendimento-distribuicoes-amortizacoes')

content = req.content

soup = BeautifulSoup(content, 'html.parser')
tabela = soup.find(name='table')
table_str = str(tabela)
df = pd.read_html(table_str)
print(df)

