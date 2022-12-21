import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
response = requests.get('https://fiis.com.br/noticias/', headers=headers)#por meio da biblioteca requests nós conseguimos importar o site

site = BeautifulSoup(response.text, 'html.parser')

noticia = site.findAll('div', attrs={'class','text-wrapper' })

for filtro in noticia:
    filtro_A = filtro.find('p', attrs={'class', 'excerpt'})
    print(filtro_A)
    filtro1 = filtro.find('a', attrs={'class', 'title'})
    print('\n', filtro1['href'])