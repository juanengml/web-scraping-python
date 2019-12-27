import scrapy 

class CitacoesSpider(scrapy.Spider):
    name = "citacoes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
        "http://quotes.toscrape.com/page/3/",
        "http://quotes.toscrape.com/page/4/",
        "http://quotes.toscrape.com/page/5/",
    ]
    
    def parse(self, response):
        for citacoes in response.css('div.quote'):
            yield {
                "texto": citacoes.css("span.text::text").extract_first(),
                "autor": citacoes.css("small.author::text").extract_first(),
                "tags": citacoes.css("div.tag a.ta::text").extract,
            }