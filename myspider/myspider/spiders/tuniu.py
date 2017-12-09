# -*- coding: utf-8 -*-
import scrapy


class TuniuSpider(scrapy.Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']
    start_urls = ['http://tuniu.com/']

    def parse(self, response):
        pass
