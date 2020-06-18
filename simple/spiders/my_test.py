# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-08-15 17:35:58
@UpdateDate: 2019-08-19 20:46:28
'''

["９９ｌiｂ", "99lib"]

import scrapy


class MyTestSpider(scrapy.Spider):
    name = 'my_test'
    # start_urls = ["https://www.99lib.net/book/9766/350113.htm"]
    # start_urls = ["https://www.99lib.net/book/9838/352232.htm"]
    start_urls = ["https://www.99lib.net/book/567/17847.htm"]

    def parse(self, response):
        CRLF = "\r\n"
        i = 10
        lstTitle = response.xpath('//*[@id="content"]/h2/text()').getall()
        title = "——".join(lstTitle)
        content = "第%s章 %s %s" % (i, title, CRLF * 2)
        parts = response.xpath('//*[@id="content"]/div')
        base = response.xpath('/html/head/meta[5]/@content').get()
        lstOrder = get_order(decode(base))
        i = 0
        for v in lstOrder:
            i += 1
            if v >= len(parts):
                print("error")
                continue
            part = parts[v]
            result = part.xpath('.//*')
            lines = part.xpath('string(.)').get()
            # result = part.xpath('.//text()')
            lines1 = part.xpath('.//text()').getall()
            lines2 = part.xpath('./text()').getall()
            # lines = part.xpath('.//text()').get()
            if result:
                for t in result:
                    print(t.root.tag, t.root.text)
                print("-" * 40)

            lines = lines.replace("九九藏书网", "").replace("九九藏书", "").replace("藏书网", "")
            content += lines + CRLF * 2


def decode(a):
    my_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    info = {
        1: '00000',
        2: '0000',
        3: '000',
        4: '00',
        5: '0',
        6: '',
    }
    d = ""
    for t in a:
        if t == "=":
            break
        i = my_map.find(t)
        c = bin(i)[2:]
        d += info[len(c)] + c

    i = 0
    LEN = 8
    b = ""
    while i + LEN <= len(d):
        t = int(d[i:i + LEN], 2)
        b += chr(t)
        i += LEN
    return b


def get_order(s):
    import re
    lst = re.split("[A-Z]+%", s)
    lst = list(map(int, lst))
    result = [-1 for _ in range(len(lst))]
    j = 0
    for i, v in enumerate(lst):
        if v < 3:
            result[v] = i
            j += 1
        else:
            result[v - j] = i
            j += 2
    return result
