# -*- coding:utf-8 -*-
'''
@Description: 爬取豆瓣Top250书籍
    scrapy crawl douban_book_top250 -o douban_book_top250.csv
    https://www.99lib.net/book/search.php?type=all&keyword=%E8%AE%B8%E4%B8%89%E8%A7%82%E5%8D%96%E8%A1%80%E8%AE%B0
@Author: lamborghini1993
@Date: 2019-07-30 16:59:56
@UpdateDate: 2019-09-19 10:59:42
'''

import scrapy

from ..items import DoubanBookItem


class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_book_top250'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }

    def start_requests(self):
        for x in range(10):
            rank = x * 25
            url = "https://book.douban.com/top250?start=%s" % rank
            yield scrapy.Request(url, headers=self.headers, meta={"rank": rank})

    def parse(self, response):
        rank = response.meta["rank"]
        books = response.xpath('//div[@class="indent"]//table')
        # books = response.xpath('//*[@id="content"]/div/div[1]/div/table')
        for i, book in enumerate(books):
            item = DoubanBookItem()
            item["ranking"] = rank + i + 1
            # 记住这里就算是子xpath对象，也需要加.//
            item["book_name"] = book.xpath('.//div[@class="pl2"]/a/@title').get()
            item["score"] = book.xpath('.//span[@class="rating_nums"]/text()').get()
            item["score_num"] = book.xpath('.//span[@class="pl"]/text()').re(r'(\d+)人评价')[0]
            item["info"] = book.xpath('.//p[@class="pl"]/text()').get()
            img_url = book.xpath(".//img/@src").get()
            print(item["ranking"], item["book_name"], img_url, sep=" | ")
            yield item
