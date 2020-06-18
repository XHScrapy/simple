# -*- coding:utf-8 -*-
'''
@Description: scrapy debug
@Author: lamborghini1993
@Date: 2019-07-30 17:34:28
@UpdateDate: 2019-08-19 19:35:48
'''

import os
import sys

from scrapy.cmdline import execute

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
execute(["scrapy", "crawl", "my_test"])
