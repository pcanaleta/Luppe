# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import logging
import pymongo

class LuppebotPipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.connection['fcf']
        self.collection = db['actes']
    
    def process_item(self, item, spider):
        #Como saber si tiene nombre de jugador y nombre de equipo
        #{nom: {$exists:true, $not: {$size:1}}}
        #{$and: [ { nom: null},{equip:null}]}
        query_existeix_jugador = {"nom": dict(item)['nom']}
        query_es_null = {"$and":[{"nom": "null"},{"equip":"null"}]}
        if self.collection.count_documents(query_existeix_jugador) > 0:
            pass
        else:
            if item['equip'] is None:
                pass
            else:
                self.collection.insert_one(dict(item))
        