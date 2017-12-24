# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class TuniuSpider(scrapy.Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']
    # start_urls = ['http://www.tuniu.com',
    # start_urls = ['http://www.tuniu.com/guide/d-sanya-906/?pcat=67']
    start_urls = ['http://www.tuniu.com/g906/whole-bj-6/list-l906-h0-i-j0_0/?pcat=67']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        with open('tuniu.txt', 'w') as f:
            for i in soup.select('span[class="main-tit"]'):
                f.write(i.text)

        #div.tnPrice > em
        #niuren_list > div.contentcontainer.clearfix > div.main.fl > div.thelist.an_mo > ul > li:nth-child(1) > div > a > div.priceinfo > div.tnPrice > em
