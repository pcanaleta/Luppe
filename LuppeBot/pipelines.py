# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import logging
import pymongo
from sqlalchemy import true

class LuppebotPipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.connection['fcf']
        self.collection = db['actes']
    
    def process_item(self, item, spider):

        #if self.collection.find_one({"nom": item['nom']}):
        #    logging.warning("EXISTEIX!!!!!!!")
        #else:
        self.collection.insert_one(dict(item))
        
        return item
