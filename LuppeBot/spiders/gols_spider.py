import scrapy
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter

# scrapy crawl --nolog --output -:json gols
# scrapy crawl gols -o Gols.csv
# scrapy crawl gols -o Gols.json

class ResidentialRecordsSpider(scrapy.Spider):
    name = "gols"

    def start_requests(self):
        urls = [
            'https://www.fcf.cat/golejadors/2022/futbol-11/tercera-catalana/grup-18'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        files = response.xpath('//*[@id="gols_grup"]//tbody//tr')

        for fila in files:
            yield {
                'Posicio' : fila.xpath('td[1]//text()').extract_first(),
                'Jugador' : fila.xpath('normalize-space(td[2]//a//text())').extract(),
                'Equip' : fila.xpath('normalize-space(td[4]//a//text())').extract(),
                'Gols(p)' : fila.xpath('td[5]//text()').extract_first(),
                'Partits jugats' : fila.xpath('td[6]//text()').extract_first(),
                'Gols partit' : fila.xpath('td[7]//text()').extract_first(),
            }
