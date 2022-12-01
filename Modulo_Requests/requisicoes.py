import requests
# Este header permite que consigamos conectar com o site simulando um usuário de navegador padrão
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
response = requests.get('https://investidor10.com.br/fiis/rankings/', headers=headers)#por meio da biblioteca requests nós conseguimos importar o site
print('Status Code:', response.status_code)
print('Header')
print(response.headers)
