## Usando re.compile e re.IGNORECASE
import re

text = "Em verdade vos digo, que conhecereis a verdade, e a verdade vos libertará."

padrao = re.compile("vos", re.IGNORECASE)

resultado = re.findall(padrao,text)

print(resultado)

## usando pipe | re.compile

pattern = re.compile(r"(segunda|terça|quarta|quinta|sexta)-feira")

samba = "Na segunda-feira eu não vou trabalhar, na terça-feira não vou trabalhar e "

print(re.findall(pattern, samba))

## find ANA

pattern = re.compile("ana")
texto = "Ana adora ouvir chiquete com banana, gosta de bananada e tambem banana, ela é irmão de mariana"
print("find ana",re.findall(pattern,texto))

## find ANA com re.I

pattern = re.compile("ana",re.I)
texto = "Ana adora ouvir chiquete com banana, gosta de bananada e tambem banana, ela é irmão de mariana"
print("find ana com re.I",re.findall(pattern,texto))

## exemplo padrão ".ato" = qualquer caracter + ato

padrao = re.compile(r".ato")
texto = "Eu tenho um gato que corre com ratos foge para o mato e eu ainda pego o sapato e um barato ele no ato"
resultado = re.findall(padrao,texto)
print(resultado)

## exemplo padrão ".ato" = qualquer caracter + ato + re.IGNORECASE

padrao = re.compile(r".ato",re.I)
texto = "Eu tenho um GATO que corre com rAtos foge para o mato e eu ainda pego o sapato e um barato ele no ato"
resultado = re.findall(padrao,texto)
print(resultado)


## exemplos de re.search() e re.match()
padrao = re.compile(r".ato")
texto = "Eu tenho um GATO que corre com rAtos foge para o mato e eu ainda pego o sapato e um barato ele no ato"
resultado = re.search(padrao,texto)
print("re.search",resultado)
texto = "gato que corre com RATO foge para o mato e eu ainda pego o sapato e um barato ele no ato"
resultado = re.match(padrao,texto)
print("re.match",resultado)


