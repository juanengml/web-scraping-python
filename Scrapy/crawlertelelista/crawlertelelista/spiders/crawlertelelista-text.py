import scrapy
import requests
import os
import logging

class SpiderTelelista(scrapy.Spider):
    try:
        name = "telelista"

        def __init__(self, url=''):
            super(SpiderTelelista, self).__init__()

            url_desmontada = url.split("/")
            self.ramo_atividade = url_desmontada[5]
            self.url = url

        def start_requests(self):
            yield scrapy.Request(url=self.url, callback=self.parse)

        def parse(self, response):
            if response.url.count("/") == 5:
                link_desmontado = response.url.split("/")
                uf_busca = link_desmontado[3]
                cidade_busca = link_desmontado[4]
                cidade_busca = cidade_busca.replace("+", " ")
                proxima_pagina = response.xpath('//link[contains(@rel, "next")]/@href').extract_first()
                page = response.url
                if page != "https://www.telelistas.net/" + uf_busca:
                    nomes = response.xpath('//td[@class="nome_resultado_ag"]//a/text()').extract()
                    telefones = response.xpath('//td[@class="text_resultado_ib" and (contains(text(),"Tel") or contains(text(),"PABX") or contains(text(),"Cel") or contains(text(),"Fax"))]/text()').extract()
                    if len(nomes) > 0 and len(telefones) > 0:
                        tels = []
                        for telefone in telefones:
                            telefone = telefone.replace("PABX", "Tel").replace("Cel", "Tel").replace("Fax", "Tel")
                            if "Tel" in telefone:
                                tels.append(telefone)

                        if len(nomes) == len(tels):
                            imagens = response.xpath('//td[@class="text_resultado_ib"]//img/@src').extract()
                            enderecos = response.xpath('//td[@class="text_endereco_ib"]/text()').extract()
                            #duas de endereço linhas por cliente
                            x = 0
                            y = 0
                            for nome in nomes:
                                imagem = requests.get(imagens[x])
                                nome_arquivo_imagem = gerar_nome_imagem(uf_busca, nome)
                                with open(nome_arquivo_imagem, 'wb') as f:
                                    f.write(imagem.content)
                                gravar_telefone(uf_busca, cidade_busca, nome, enderecos[y] + " " + enderecos[y + 1], self.ramo_atividade, tels[x], nome_arquivo_imagem)
                                x += 1
                                y = y + 2
                        else:
                            for nome in nomes:
                                with open("nao_processado.txt", "a") as arquivo:
                                    arquivo.write("\nNome: " + nome + " - " + uf_busca + " " + cidade_busca)
                            for tel in tels:
                                with open("nao_processado.txt", "a") as arquivo:
                                    arquivo.write("\nTelefone: " + tel + " - " + uf_busca + " " + cidade_busca)

                    #Mais telefones ou ver telefone
                    mais_telefones = response.xpath('//td[@class="text_resultado_ib"]//a/@href').extract()
                    for mais_tel in mais_telefones:
                        yield response.follow(mais_tel, callback=self.parse)

                if proxima_pagina:
                    yield response.follow(proxima_pagina, callback=self.parse)
            else:
                #pagina individual - mais telefones ou ver telefone
                link_desmontado = response.url.split("/")
                uf_busca = link_desmontado[4]
                cidade_busca = link_desmontado[5]
                cidade_busca = cidade_busca.replace("+", " ")
                nome = response.xpath('//h1[contains(@class,"nome_anun")]/text()').extract()
                telefones = response.xpath('//div[@id="telInfo"]//span/text()').extract()
                imagens = response.xpath('//div[@id="telInfo"]//span//img/@src').extract()
                endereco = response.xpath('//input[contains(@id,"enderecoreg")]/@value').extract()
                #numero = response.xpath('//input[contains(@id,"numeroreg")]/@value').extract()
                endereco_completo = response.xpath('//div[contains(text(),"' + endereco[0] + '")]/text()').extract()
                endereco_final = None
                for endereco in endereco_completo:
                    if endereco_final:
                        endereco_final = endereco_final + " - " + endereco
                    else:
                        endereco_final = endereco
                x = 0
                for telefone in telefones:
                    imagem = requests.get(imagens[x])
                    nome_arquivo_imagem = gerar_nome_imagem(uf_busca, nome[0])
                    with open(nome_arquivo_imagem, 'wb') as f:
                        f.write(imagem.content)
                    gravar_telefone(uf_busca, cidade_busca, nome[0], endereco_final, self.ramo_atividade, telefone, nome_arquivo_imagem)
                    x += 1
    except:
        logging.info("Erro na funcao principal")

def limpar_telefone(telefone):
    if telefone:
        if "Tel:" in telefone:
            telefone = telefone.split("Tel:")
            telefone = telefone[1]
        return telefone

def limpar_campo(campo):
    campo = campo.replace("'", "").replace(",", "").replace("%20", " ").strip().strip("\n\r")
    campo = campo.replace('\n', ' ').replace('\r', '').replace('?',''.replace(' ',''))
    return campo

def gerar_nome_imagem(uf_busca, imagem):
    imagem = limpar_campo(imagem)
    imagem_original = limpar_campo(imagem)
    if not os.path.exists('C:\\Temp\\imagens_capturadas\\' + uf_busca):
        os.mkdir('C:\\Temp\\imagens_capturadas\\' + uf_busca)

    contador = 0
    while True:
        if not os.path.exists('C:\\Temp\\imagens_capturadas\\' + uf_busca + '\\' + imagem + '.jpg'):
            return 'C:\\Temp\\imagens_capturadas\\' + uf_busca + "\\" + imagem + ".jpg"
        else:
            contador += 1
            imagem = imagem_original + str(contador)

def gravar_telefone(uf, cidade, nome, endereco, ramo_atividade, tel, nome_arquivo_imagem):
    with open("telefones_capturados.txt", "a") as arquivo:
        arquivo.write("\n" + uf + " - " + cidade + " - " + nome + " - " + endereco + " - " +
                      ramo_atividade + " - " + tel + " - " + nome_arquivo_imagem)

