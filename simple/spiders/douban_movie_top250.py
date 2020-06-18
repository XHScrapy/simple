# -*- coding:utf-8 -*-
'''
@Description: 爬取豆瓣Top250电影
    scrapy crawl douban_movie_top250 -o douban_movie_top250.csv
@Author: lamborghini1993
@Date: 2019-07-30 16:59:56
@UpdateDate: 2019-08-01 16:08:56
'''

import scrapy

from ..items import DoubanMovieItem


class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    m_Url = 'https://movie.douban.com/top250/'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }

    def start_requests(self):
        yield scrapy.Request(self.m_Url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item["ranking"] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item["movie_name"] = movie.xpath('.//span[@class="title"]/text()').extract()[0]
            item["score"] = movie.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            item["score_num"] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = self.m_Url + next_url[0]
            yield scrapy.Request(next_url, headers=self.headers)
