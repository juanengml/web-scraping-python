from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def abrir_paginas(url_da_pagina):
    global paginas
    global paginas_invalidas

    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html,"html.parser")
    except:
        paginas_invalidas.add(nova_pagina)
