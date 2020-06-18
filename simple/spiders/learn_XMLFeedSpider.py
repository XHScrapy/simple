# -*- coding:utf-8 -*-
'''
@Description: 学习XMLFeedSpider
https://docs.scrapy.org/en/latest/topics/spiders.html
@Author: lamborghini1993
@Date: 2019-08-08 14:21:07
@UpdateDate: 2019-08-08 14:23:17
'''

from scrapy.spiders import XMLFeedSpider
from ..items import TestItem


class MySpider(XMLFeedSpider):
    name = 'learn_XMLFeedSpider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        item = TestItem()
        item['id'] = node.xpath('@id').get()
        item['name'] = node.xpath('name').get()
        item['description'] = node.xpath('description').get()
        return item
