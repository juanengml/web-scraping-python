from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def abrir_pagina(url_da_pagina):
    global paginas
    global nova_pagina

    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html, "html.parser")

            for link in bsObj.findAll("a"):
                if "href" in link.attrs:
                    #print(link.attrs)
                    if link.attrs['href'] not in paginas and link.attrs['href'] not in paginas_invalidas:
                        nova_pagina = link.attrs['href']
                        print(nova_pagina)
                        paginas.add(nova_pagina)
                        abrir_pagina(nova_pagina)
    except:
        paginas_invalidas.add(nova_pagina)

print(abrir_pagina("http://juanengml2019utfpr.pythonanywhere.com/"),"\n")
print(abrir_pagina("http://e-m-b.org/"))