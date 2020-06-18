# -*- coding:utf-8 -*-
'''
@Description: 获取代理IP
    scrapy crawl get_proxy -a page=1
@Author: lamborghini1993
@Date: 2019-08-16 11:25:18
@UpdateDate: 2019-08-16 14:07:46
'''


import scrapy


class GetProxySpider(scrapy.Spider):
    name = 'get_proxy'
    hears = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Referer": "https://www.xicidaili.com/nn/1",
    }

    def __init__(self, page = 4, **kwargs):
        super().__init__(**kwargs)
        self.m_Page = int(page)

    def start_requests(self):
        for i in range(self.m_Page):
            url = "https://www.xicidaili.com/nn/%s" % (i + 1)
            yield scrapy.Request(url, headers=self.hears)

    def parse(self, response):
        ips1 = response.xpath('//table[@id="ip_list"]')
        txt1 = ips1.get()
        ips2 = response.xpath('//table[@id="ip_list"]/tbody')
        ips = response.xpath('//table[@id="ip_list"]/tr')
        for i in range(1, len(ips)):
            tr = ips[i]
            ip = tr.xpath('./td[2]/text()').get()
            port = tr.xpath('./td[3]/text()').get()
            http = tr.xpath('./td[6]/text()').get()
            time = tr.xpath('./td[9]/text()').get()

            print(f"{http}://{ip}:{port}  {time}")
