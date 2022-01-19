import scrapy
import os

class GenerateUrlSpider(scrapy.Spider):
    name = 'generate_url'
    start_urls = ['https://www.fcf.cat/resultats/2022/futbol-11/quarta-catalana/grup-1/jornada-1']

    def parse(self, response):
        link_competicio = response.xpath('//*[@id="select_competi"]/option/@value').getall()
        yield from response.follow_all(link_competicio, self.parse_link_grups)
    
    def parse_link_grups(self, response):
        link_grupo = response.xpath('//*[@id="select_grupo"]/option/@value').getall()
        link_jornada = response.xpath('//*[@id="select_jornada"]/option/@value').getall()
        if not os.path.isdir('./log.txt'):
            with open('urls_fcf.txt','a') as f:
                for grupo in link_grupo:
                    for jornada in link_jornada:
                        f.write(grupo+jornada + "\n")