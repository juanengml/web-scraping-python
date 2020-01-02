import requests


payload = {
    "email":"juancavancante@dasilva.com",
    "assunto":"Email enviado pelo robo",
    "mensagem":"Este email foi enviado por um robo"
}

headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.post("http://juanengml2019utfpr.pythonanywhere.com/contact", headers=headers, data=payload)


print(r.text)