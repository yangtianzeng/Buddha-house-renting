# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.utils.project import get_project_settings
class HomeproPipeline(object):
    def process_item(self, item, spider):
        return item

    def process_item(self, item, spider):
        insert_sql = "insert into {0}({1}) values ({2})".format(self.sqlite_table,
                                                                ', '.join(item.fields.keys()),
                                                                ', '.join(['?'] * len(item.fields.keys())))
        self.cur.execute(insert_sql, item.fields.values())
        self.conn.commit()

        return item



from scrapy.utils.project import get_project_settings
class Sqlite3Pipeline(object):
    def open_spider(self,spider):
        settings = get_project_settings()
        name = settings['SQLITE_TABLE']
        self.db = sqlite3.connect(settings['SQLITE_FILE'])
        self.cur = self.db.cursor()


    def close_spider(self,spider):
        self.db.close()


    def process_item(self,item,spider):
        self.save_to_sqlite(item)
        return item

    def save_to_sqlite(self, item):
        # 拼接sql语句
        sql = 'insert into houseinfo(id,city,title,price,paytype,renttype,hometype,area,decorade,region,address,linkman,phone,img,features) values(NULL,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
        item['city'], item['title'], item['price'], item['paytype'], item['renttype'], item['hometype'],item['area'], item['decorade'],item['region'],item['address'],item['linkman'],item['phone'],item['img'],item['features'])
        # 执行sql语句
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        return item