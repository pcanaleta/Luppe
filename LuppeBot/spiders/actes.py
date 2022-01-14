import logging
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

    start_urls = ['https://www.fcf.cat/resultats/2022/futbol-11/tercera-catalana/grup-18/jornada-14']

    def parse(self, response):
        actes_page_links = response.css('td.p-5.resultats-w-resultat.tc a')
        yield from response.follow_all(actes_page_links, self.parse_acta)

        #pagination_links = response.css('li.next a')
        #yield from response.follow_all(pagination_links, self.parse)

    def parse_acta(self, response):
        actes = response.xpath('//*[@class="col-md-12 bg-white mb-20"]')
        blocs = response.xpath('//*[@class="col-md-4 p-0_ml"]//table')

        #item = Equip()
        #item['nom'] = blocs.xpath('//th/text()').extract()
        #yield item
        item = Jugador()
        item['nom'] = actes.xpath('//*[@class="col-md-12 bg-white mb-20"]//table//tbody//tr//td//a/text()').extract()
        yield item
        #for acta in actes:
        #    if response.xpath('//*[@class="col-md-4 p-0_ml"]//table//th/text()').extract() == 'Titulars':
        #        item = Jugador()
        #        item['nom'] = acta.xpath('//*[@class="col-md-12 bg-white mb-20"]//table//tbody//tr//td//a/text()').extract()
        #        yield item