import requests #importa a biblioteca requests
from bs4 import BeautifulSoup

# Este header permite que consigamos conectar com o site simulando um usuário de navegador padrão
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
response = requests.get('https://valorinveste.globo.com/cotacoes/', headers=headers)#por meio da biblioteca requests nós conseguimos importar o site

content = response.content

site = BeautifulSoup(content, 'html.parser')
noticia = site.find('div', attrs={'class': 'vd-automatic-tables cell medium-24 valor-data__mobile-break'})
print(noticia.prettify())
