import re

padrao = r'[\w.-]+@[\w.-]+'
texto = "juanengml@gmail.com\neven@evd.edu\ntdc@asdasdasd.com\naosdkasdqwueqwej12o3i123oiaosidao3hoi123h41i4h13nfwsjskjsnkfjsndfitwjoeirj2342342sdsfsdf@sfsdfsdfsdfsfsdcxvxvwerw.com\n\n"
matcher = re.findall(padrao,texto)
print(matcher)