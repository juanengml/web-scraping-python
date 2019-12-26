import re
from os import system

texto = r"""
Relação dos candidatos - concurso pu
"""
# PDF convertido em TXT https://depsec.unifap.br/intranet/arquivos/arq3662.pdf
system("ls ")
texto = open('arq3662.txt').read()

padrao = re.compile("([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")

resultado = re.findall(padrao,texto)
print("CPFS localizados no arquivo,",resultado)
