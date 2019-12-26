from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitulo(url):
    ## TRATANTO ERROS COM URL
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print("{ª_ª} Erro de HTTP: ",erro)
        return None
    except URLError as erro:
        print("{º_º} Erro na url: ",erro),
        return None
    except:
        print(" {/\ __ /\ } Erro gato triste ")
        return None
    ## TRATANTO ERROS COM beautifulsoup
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print("eRRO NA TAG H1\n:",erro)
        return None
    return titulo

titulo = getTitulo(input("informe url: "))

if titulo is not None:
    print(titulo)
else:
    print("Titulo não exonctroado")