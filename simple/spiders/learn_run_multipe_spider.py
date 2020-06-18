# -*- coding:utf-8 -*-
'''
@Description: 学习运行多个爬虫程序在同一个进程中
@Author: lamborghini1993
@Date: 2019-08-09 14:29:37
@UpdateDate: 2019-08-09 15:09:55
'''

import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider1(scrapy.Spider):
    name = "MySpider1"
    start_url = ["https://www.zhihu.com/hot"]

    def parse(self, response):
        for hotItem in response.xpath('//div[@class="HotList-list"]/section'):
            index = hotItem.xpath('//div[@class="HotItem-index"]/div/text()').get()
            title = hotItem.xpath('//div[@class="HotItem-content"]/a/@title').get()
            print(f"知乎:{index}-{title}")


class MySpider2(scrapy.Spider):
    name = "MySpider2"
    start_url = ["http://lamborghini1993.xyz/archives/"]

    def parse(self, response):
        for archive in response.xpath('//div[@class="posts-collapse"]/article'):
            title = archive.xpath('./header/h2/a/span/text()').get()
            data = archive.xpath('./header/div/time/@content').get()
            print(f"博客:{data}-{title}")


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider1)
    process.crawl(MySpider2)
    process.start()
