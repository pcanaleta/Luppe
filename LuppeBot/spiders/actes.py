import logging
from fsspec import Callback
import scrapy
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
from scrapy.linkextractors import LinkExtractor
from LuppeBot.items import Jugador, Equip

# scrapy crawl --nolog --output -:json gols
# scrapy crawl gols -o Gols.csv
# scrapy crawl gols -o Gols.json

class ResidentialRecordsSpider(scrapy.Spider):
    name = 'actes'
    categoria = {}

    #start_urls = [l.strip() for l in open('listofurls.txt').readlines()]
    start_urls = ['https://www.fcf.cat/resultats/2022/futbol-11/tercera-catalana/grup-18/jornada-14']

    def parse(self, response):
        actes_page_links = response.css('td.p-5.resultats-w-resultat.tc a')
        yield from response.follow_all(actes_page_links, self.parse_acta)

        #pagination_links = response.css('li.next a')
        #yield from response.follow_all(pagination_links, self.parse)

    def parse_acta(self, response):
        jugadors_page_links = response.css('table.acta-table a')
        yield from response.follow_all(jugadors_page_links, self.parse_jugador)
    
    def parse_jugador(self, response):

        item = Jugador()
        item['nom'] = response.xpath('//*[@class="m-0 fs-30 va-b bold"]/text()').extract_first()
        item['equip'] = response.xpath('//*[@class="mt-5 fs-20 va-t darkgrey italic"]/text()').extract_first()
        item['jornades_lliga'] = response.xpath('//*[@class="axis"]//div/text()').extract_first()
        item['convocat'] = response.xpath('//*[@class="bar teal"]//*[@class="percent"]/text()').extract_first()
        item['titular'] = response.xpath('//*[@class="bar salmon"]//*[@class="percent"]/text()').extract_first()
        item['suplent'] = response.xpath('//*[@class="bar peach"]//*[@class="percent"]/text()').extract_first()
        item['jugats'] = response.xpath('//*[@class="bar lime"]//*[@class="percent"]/text()').extract_first()
        item['gols'] = response.xpath('//div[@class="gol"]//div[@class="comptador"]/text()').extract_first()
        item['gols_partit'] = response.css('span.fs-30::text').extract_first()
        item['targetes_grogues'] = response.css('div.groga-s div::text').extract_first()
        item['targetes_vermelles'] = response.css('div.vermella-s div::text').extract_first()
        item['targetes_dobles_grogues'] = response.css('div.groga-vermella-s div.comptador::text').extract_first()
        yield item