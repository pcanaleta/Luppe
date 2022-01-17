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

    #collection_name = 'actes'
    spider = None

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        #Como saber si tiene nombre de jugador y nombre de equipo
        #{nom: {$exists:true, $not: {$size:1}}}
        #{$and: [ { nom: null},{equip:null}]}
        self.spider = spider
        query_es_null = {"$and":[{"nom": "null"}, {"equip": "null"}]}
        query_existeix_jugador = {"nom": dict(item)['nom']}
        query_mateixa_categoria = {"categoria": item['categoria']}
        list_of_collections = self.db.list_collection_names()
        #if self.db[item['categoria']].count_documents(query_existeix_jugador) > 0:
        #else:
        if not (item['equip'] == None):
            self.db[item['categoria']].update_one(
                {"id": item['id']},
                {"$set": dict(item)},
                upsert=True
            )                         
            return item
        
          
#