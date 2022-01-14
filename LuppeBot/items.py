# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Actes(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titol_acte = scrapy.Field()
    pass

class TaulaGolsItem(scrapy.Item):

    posicio = scrapy.Field()
    jugador = scrapy.Field()
    equip = scrapy.Field()
    gols_penal = scrapy.Field()
    partits_jugats = scrapy.Field()
    gols_partit = scrapy.Field()
    pass

class Jugador(scrapy.Item):
    numero = scrapy.Field()
    nom = scrapy.Field()
    cognom = scrapy.Field()
    targetes_grogues = scrapy.Field()
    targetes_vermelles = scrapy.Field()
    targetes_dobles_grogues = scrapy.Field()
    gols = scrapy.Field()
    gols_partit = scrapy.Field()
    equip = scrapy.Field()
    pass

class Equip (scrapy.Item):
    nom = scrapy.Field()
    pass
