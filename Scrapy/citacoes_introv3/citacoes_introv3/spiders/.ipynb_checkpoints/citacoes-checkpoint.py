import scrapy 



class CitacoesSpider(scrapy.Spider):
    name = "citacoes"
    
    start_url = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
        "http://quotes.toscrape.com/page/3/",
        "http://quotes.toscrape.com/page/4/",
        "http://quotes.toscrape.com/page/5/",
    ]
    
    def parse(self, response):
        for citacao in response.css("div.quote"):
            yield {
                'texto':citacao.css('span.text::text').extract_first(),
                'autor':citacao.css('span.author::text').extract_first(),                
            }