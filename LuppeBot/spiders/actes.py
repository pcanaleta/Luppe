from gc import collect
import logging
from fsspec import Callback
import scrapy
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
from scrapy.linkextractors import LinkExtractor
from LuppeBot.items import Jugador, Equip
import os

# scrapy crawl --nolog --output -:json gols
# scrapy crawl gols -o Gols.csv
# scrapy crawl gols -o Gols.json

class ResidentialRecordsSpider(scrapy.Spider):
    
    name = 'actes'

    start_urls = [l.strip() for l in open('urls_fcf.txt').readlines()]
    #start_urls = ['https://www.fcf.cat/resultats/2022/futbol-11/quarta-catalana/grup-1/jornada-1']
    
    #Metodo para conseguir sacar la información de todas las categorias
    def parse(self, response):
        actes_page_links = response.xpath('//tr[@class="linia"][contains(.," - ")]//td[@class="p-5 resultats-w-resultat tc"]//a')
        yield from response.follow_all(actes_page_links, self.parse_acta)

    def parse_acta(self, response):
        jugadors_page_links = response.xpath('//table[@class="acta-table"][contains(.,"Titulars") or contains(.,"Suplents")]//a')
        yield from response.follow_all(jugadors_page_links, self.parse_jugador)
    
    def parse_jugador(self, response):
        item = Jugador()
        if len((response.url).split('/')) > 6:
            item['id'] = response.url.split('/')[8] + "_" + response.url.split('/')[9]
            item['categoria'] = response.url.split('/')[6] + "_" + response.url.split('/')[7] + "_" + response.url.split('/')[4]
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