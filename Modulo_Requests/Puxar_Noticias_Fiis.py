import requests #importa a biblioteca requests
from bs4 import BeautifulSoup #importa a biblioteca BeautifulSoup
import pandas as pd #importa a biblioteca pandas

lista_noticias = [] #variável que receberá a lista de noticias

# Este header permite que consigamos conectar com o site simulando um usuário de navegador padrão
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
response = requests.get('https://fiis.com.br/noticias/', headers=headers)#por meio da biblioteca requests nós conseguimos importar o site

content = response.content #content recebe a variável response que faz o get no site indicado

site = BeautifulSoup(content, 'html.parser') #site recebe BeatifulSoup com content(conteúdo do site) juntamente com a extensão do site (html)

noticias = site.findAll('div', attrs={'class': 'text-wrapper'}) #noticias recebe o site com o comando FindAll(busque em todo o arquivo), 
                                                                #filtre o termo 'div' e os atributos(attrs) |class e text-wrapper| disponíveis no site

#procure dentro da variável noticias as variáveis titulo e link
for noticia in noticias:
    titulo = noticia.find('p', attrs={'class': 'excerpt'})
    link = noticia.find('a', attrs={'class': 'title'})

    lista_noticias.append([titulo.text, link['href']]) #coloque em listas as duas variáveis

news = pd.DataFrame(lista_noticias, columns=['Título da Noticia','Links']) #news recebe pd (pandas) dentro de um dataframe a variável lista_noticias
                                                                           #coloque no nome das colunas o "titulo da noticia" e "links"

news.to_csv('noticiasfiis.csv', index=False) #exporte para csv sem index (indesx=false)