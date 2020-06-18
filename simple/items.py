# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SimpleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()    # 排名
    movie_name = scrapy.Field() # 电影名
    score = scrapy.Field()      # 评分
    score_num = scrapy.Field()  # 打分人数


class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()


class DoubanBookItem(scrapy.Item):
    ranking = scrapy.Field()    # 排名
    book_name = scrapy.Field() # 电影名
    score = scrapy.Field()      # 评分
    score_num = scrapy.Field()  # 打分人数
    info = scrapy.Field()  # 详细信息
