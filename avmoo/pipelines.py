# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from .models import Starinfo, engine
from datetime import datetime

class AvmooPipeline(object):
    def process_item(self, item, spider):
        if item['height']:
            item['height'] = int(item['height'])
        if item['birthday']:
            item['birthday'] = datetime.strptime(item['birthday'], '%Y-%m-%d')
        self.session.add(Starinfo(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()



