### Com urllib
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
"""
html = urlopen("http://www.wingsec.com")
print(f"Html 1: {html}")

try:
    html = urlopen("http://www.wingsec.com/erro")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)

html = urlopen("http://www.wingsec.com")
print(f"Html 3: {html}")
"""

html = urlopen("http://juanengml2019utfpr.pythonanywhere.com/")
print(html)

try:
 html = urlopen("http://juanengml2019utfpr.pythonanywhere.com/erro")
 print(html)
except HTTPError as erro:
    print(erro)
try:
    html = urlopen("http://xptooasda1322.com.br")
    print(html)
except URLError as erro:
    print(erro)

html = urlopen("http://juanengml2019utfpr.pythonanywhere.com/about")
print(html)



### TRATANDO ERROS com BeautifulSoup
from bs4 import BeautifulSoup

html = urlopen("http://juanengml2019utfpr.pythonanywhere.com/about")
bsObj = BeautifulSoup(html.read(),"html.parser")
try:
    resultado = bsObj.html.table.h1
except AttributeError as erro:
    print("N existe tabela cacete")









