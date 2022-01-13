# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LuppebotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TaulaGolsItem(scrapy.Item):

    posicio = scrapy.Field()
    jugador = scrapy.Field()
    equip = scrapy.Field()
    gols_penal = scrapy.Field()
    partits_jugats = scrapy.Field()
    gols_partit = scrapy.Field()
    pass
