import scrapy
import logging as log


class RusprofileSpider(scrapy.Spider):
    name = 'rusprofile'
    #allowed_domains = ['rusprofile.ru']
    #start_urls = ['https://www.rusprofile.ru/codes/429110']

    def start_requests(self):
        #urls = [
        #    'https://www.rusprofile.ru/codes/89220',
        #    'https://www.rusprofile.ru/codes/429110'
        #]
        urls = ['https://www.rusprofile.ru/codes/89220']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_main)

    def parse_main(self, response):
        for i in response.css('div.company-item'):
            company = i.css('div.company-item__title a::attr("href")').get()
            #log.info(f'компания - {company}')
            yield response.follow(company, callback=self.parse_data)
        pages = response.css('a.nav-next::attr("href")').get()
        if not pages is None:
            yield response.follow(pages, self.parse_main)        
        
    def parse_data(self, response):
        response_dict = {'title': response.css('div.company-name::text').get().strip()}
        #log.info(f'название - {response_dict["title"]}')
        yield response_dict