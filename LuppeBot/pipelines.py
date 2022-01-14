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
        self.collection.insert_one(dict(item))
        #valid = True
        #for data in item:
        #    if not data:
        #        valid = False
        #        raise DropItem("Missing {0}!".format(data))
        #if valid:
       #self.collection.inser
            #self.collection.insert_one(dict(item))
            #logging.warning("Question added to MongoDB database!",
            #    level=logging.DEBUG, spider=spider)
        return item
