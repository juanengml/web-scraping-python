import re
from datetime import datetime

print(datetime.now())
padrao = re.compile(r"\d{2}/\d{2}/\d{4}")
texto = "Hoje e dia xpqtop 26/23/2023"
print(texto)
print(re.findall(padrao,texto))
data_atual = str(datetime.now())
padrao2 = re.compile(r"\d{4}-\d{2}-\d{2}")
print(re.findall(padrao2,data_atual))
print(data_atual)