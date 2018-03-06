# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvpjtSpider(CSVFeedSpider):
    name = 'mycsvpjt'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        #i['url'] = row['url']
        i['name'] = row['name'] 
        i['sex'] = row['sex']
        print(i['name'])
        print (i['sex'])
        #i['description'] = row['description']
        return i