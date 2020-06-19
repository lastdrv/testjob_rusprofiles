import scrapy
import logging as log


class RusprofileSpider(scrapy.Spider):
    name = 'rusprofile'
    #allowed_domains = ['rusprofile.ru']
    #start_urls = ['https://www.rusprofile.ru/codes/429110']

    def start_requests(self):
        urls = [
            'https://www.rusprofile.ru/codes/89220',
            'https://www.rusprofile.ru/codes/429110'
        ]
        #urls = ['https://www.rusprofile.ru/codes/12200']
        for url in urls:
            self.okved = url.split('/')[-1]
            yield scrapy.Request(url=url, callback=self.parse_main) # url.split('/')[-1]

    def parse_main(self, response):
        for i in response.css('div.company-item'):
            company = i.css('div.company-item__title a::attr("href")').get()
            yield response.follow(company, callback=self.parse_data)
        pages = response.css('a.nav-next::attr("href")').get()
        if not pages is None:
            yield response.follow(pages, self.parse_main)        
        
    def parse_data(self, response):
        moneys_test = response.xpath('//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[2]/dd/span/text()').get()
        if moneys_test:
            moneys_test = int(''.join(moneys_test[:-4].split()))
        response_dict = {
            'okved': self.okved
            'title': response.css('div.company-name::text').get().strip(),
            'ogrn': response.xpath('//*[@id="clip_ogrn"]/text()').get(),
            'okpo': int(response.css('#clip_okpo::text').get()),
            'status': response.css('div.company-status').attrib['class'].split()[-1],
            'regdate': ''.join(response.xpath('//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd/text()').get().split('.')[::-1]),
            'moneys': moneys_test,
            }
        print(response_dict)
        yield response_dict