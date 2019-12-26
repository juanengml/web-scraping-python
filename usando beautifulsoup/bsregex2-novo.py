from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

# Erro 403 porque alguns sites tratam scraping
#html = urlopen("http://www.tudogostoso.com.br")

# Conteúdo sobre user-agent:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/User-Agent
# O cabeçalho de requisição User-Agent contém uma string característica
# que permite o protocolo de rede do cliente identificar o tipo de aplicação,
# sistema operacional, fornecedor do software ou versão do software do agente
# de usuário do software solicitante.
#req = Request("http://www.tudogostoso.com.br", headers={'User-Agent': 'Mozilla/5.0'})
#req = Request("https://www.tudogostoso.com.br", headers={'User-Agent' : '*'})
req = Request("https://evaldowolkers.wordpress.com/python-web-scraping-aula-05-um-pouco-mais-de-beautifulsoup/")

html = urlopen(req).read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("a", {"href":re.compile("/categorias/")})

for link in links:
    print(link["href"])

