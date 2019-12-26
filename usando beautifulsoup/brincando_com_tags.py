from urllib.request import urlopen
from bs4 import BeautifulSoup



html = urlopen("http://juanengml2019utfpr.pythonanywhere.com")
bjObj = BeautifulSoup(html,"html.parser")



print(bjObj.get_text())
print(bjObj.title)
print(bjObj.title.name)
#print(bjObj.title.name.string)

print(bjObj.title.parent)
print(bjObj.title.parent.name)
print(bjObj.body.a['href'])