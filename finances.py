'''!pip install yfinance'''

from datetime import datetime
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import plotly
import openpyxl

url ='https://www.fundsexplorer.com.br/ranking'

'''
- response recebe requests com a função get(url)
- soup recebe a função beatifulsoup + response em formato de texto (.text) e xml
- table recebe soup + find_all = procure por 'table' em todo o arquivo requisitado (soup) e armazene o primeiro valor [0]
- df recebe pd (pandas), leia o arquivo html (read_html), converta para string (str) separe algarismos decimais com ',' e milhares com '.'.'''


response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table), decimal=',', thousands='.')[0]

#colunas = df.loc[:, ['Código do fundo','Preço Atual','Dividendo','VPA','P/VPA']]

#colunas
df.to_excel('fundos_ii.xlsx')
read = pd.read_excel('fundos_ii.xlsx')
read.to_csv('fundosii.csv', decimal=',', header=True)
ac = pd.DataFrame(pd.read_csv('fundosii.csv'))

symbols = ac['Código do fundo'] + '.SA'
start = datetime(2015, 12, 1)
end = datetime.today()

def pega_fundos(name):
    stock = yf.download(name, start = start, end = end)
    return stock

stock_dict= {}

for symbol in symbols:
    try:
        stock_dict[symbol] = pega_fundos(symbol)
    except:
        print("Erro: tente novamente.")
print("Terminou")

stock_dict['BTCR11.SA']

returns = pd.concat(axis=1)

for key in stock_dict.keys():
    returns[key] = stock_dict[key]['Adj Close'].pct_change()
returns.head()
