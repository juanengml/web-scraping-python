from urllib.request import  urlopen
from bs4 import BeautifulSoup

link = "http://juanengml2019utfpr.pythonanywhere.com"
html = urlopen(link)

bsobjeto = BeautifulSoup(html.read(),"html.parser")



print (bsobjeto.h1)
#print (bsobjeto.title)
#print (bsobjeto.body.p)
for LINKS in bsobjeto.body.find_all("a"):
 data = str(LINKS.get("href"))
 print(data)