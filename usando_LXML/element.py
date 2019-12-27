from lxml import etree

# Criando um elemento denominado Teste
elemento = etree.Element("Teste")

# Adicionado um texto ao elemento Teste
elemento.text = "Este é o texto da tag Teste"

# Imprimindo o objeto criado usando etree.tostring()
print(etree.tostring(elemento))

# imprimindo a tag do objeto xml criado
print(elemento.tag)

# Imprimindo o texto da tag
print(elemento.text)