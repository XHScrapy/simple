# -*- coding:utf-8 -*-
'''
@Description: 爬取豆瓣动作片电影排行
    抓取AJAX异步加载页面
    scrapy crawl douban_movie_action_rank -o douban_movie_action_rank.csv
@Author: lamborghini1993
@Date: 2019-07-31 10:46:45
@UpdateDate: 2019-08-01 16:09:05
'''

import json

import scrapy

from ..items import DoubanMovieItem


class DoubanMovieActionRankSpider(scrapy.Spider):
    name = 'douban_movie_action_rank'
    m_Url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    m_Start = 0
    m_MaxNum = 20

    def get_next_url(self):
        url = f"https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={self.m_Start}&limit={self.m_MaxNum}"
        self.m_Start += self.m_MaxNum
        return url

    def start_requests(self):
        yield scrapy.Request(self.get_next_url(), headers=self.headers)

    def parse(self, response):
        datas = json.loads(response.body)
        if not datas:
            return
        item = DoubanMovieItem()
        for dInfo in datas:
            item["ranking"] = dInfo["rank"]
            item["movie_name"] = dInfo["title"]
            item["score"] = dInfo["score"]
            item["score_num"] = dInfo["vote_count"]
            yield item

        yield scrapy.Request(self.get_next_url(), headers=self.headers)
