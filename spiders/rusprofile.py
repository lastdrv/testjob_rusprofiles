# -*- coding: utf-8 -*-
import scrapy


class RusprofileSpider(scrapy.Spider):
    name = 'rusprofile'
    allowed_domains = ['rusprofile.ru']
    start_urls = ['http://rusprofile.ru/']

    def parse(self, response):
        pass
