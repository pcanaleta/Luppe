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
        connection = pymongo.MongoClient('cluster0-shard-00-01.2kn4u.mongodb.net',
        27017)
        db = connection['luppe']
        self.collection = db['actes']
    
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(item))
            logging.warning("Question added to MongoDB database!",
                    level=logging.DEBUG, spider=spider)
        self.collection.insert(dict(item))
        return item
