from lxml import etree

# Criando o elemento Clientes
clientes = etree.Element("clientes")

# Criando (diretamente) um subelemento do elemento clientes denominado cliente1 (tag cliente)
cliente1 = etree.SubElement(clientes, "cliente")
# Criando um subelemento do elemento cliente1 denominado nome1 (tag nome)
nome1 = etree.SubElement(cliente1, "nome")
# Definindo um texto para nome1
nome1.text = "Fulano de Marte"
idade1 = etree.SubElement(cliente1, "idade")
idade1.text = "32"
sexo1 = etree.SubElement(cliente1, "sexo")
sexo1.text = "Masculino"
cpf1 = etree.SubElement(cliente1, "cpf")
cpf1.text = "012.345.678-90"


cliente2 = etree.Element("cliente")
nome2 = etree.SubElement(cliente2, "nome")
nome2.text = "Sicrano da Terra"
# Adicionando com append o elemento cliente2 no elemento clientes (vai ser um subelemento)
idade2 = etree.SubElement(cliente2, "idade")
idade2.text = "25"
sexo2 = etree.SubElement(cliente2, "sexo")
sexo2.text = "Masculino"
cpf2 = etree.SubElement(cliente2, "cpf")
cpf2.text = "987.345.678-90"
clientes.append(cliente2)

cliente3 = etree.Element("cliente")
nome3 = etree.SubElement(cliente3, "nome")
nome3.text = "Beltrana de Betelgeuse"
# Adicionando com append o elemento cliente2 no elemento clientes (vai ser um subelemento)
idade3 = etree.SubElement(cliente3, "idade")
idade3.text = "22"
sexo3 = etree.SubElement(cliente3, "sexo")
sexo3.text = "Feminino"
cpf3 = etree.SubElement(cliente3, "cpf")
cpf3.text = "111.345.678-90"
clientes.append(cliente3)

print(etree.tostring(clientes))
print(etree.tostring(clientes, pretty_print=True))
print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))



"""
<clientes>
  <cliente>
      <nome>Fulano de Marte</nome>
      <idade>32</idade>
      <sexo>Masculino</sexo>
      <cpf>012.345.678-90</cpf>
  </cliente>
  <cliente>
      <nome>Sicrano da Terra</nome>
      <idade>25</idade>
      <sexo>Masculino</sexo>
      <cpf>987.345.678-90</cpf>
  </cliente>
  <cliente>
      <nome>Beltrana de Betelgeuse</nome>
      <idade>22</idade>
      <sexo>Feminino</sexo>
      <cpf>111.345.678-90</cpf>
  </cliente>
</clientes>

"""