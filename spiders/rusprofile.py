import scrapy


class RusprofileSpider(scrapy.Spider):
    name = 'rusprofile'


    def start_requests(self):
        """ Для каждого нужного ОКВЭД вызываем функцию парсинга parse_main()
        """
        urls = [
            'https://www.rusprofile.ru/codes/89220',
            'https://www.rusprofile.ru/codes/429110'
        ]
        for url in urls:
            self.okved = url.split('/')[-1]
            yield scrapy.Request(url=url, callback=self.parse_main)


    def parse_main(self, response):
        """ Парсим данные по конкретному ОКВЭД включая переход по страницам
        """
        for i in response.css('div.company-item'):
            company = i.css('div.company-item__title a::attr("href")').get()
            yield response.follow(company, callback=self.parse_data)
        pages = response.css('a.nav-next::attr("href")').get()
        if not pages is None:
            yield response.follow(pages, self.parse_main)        


    def parse_data(self, response):
        """ Парсим страницу с профилем организации
            Возвращает словарь для записи в БД
        """
        moneys_test = response.xpath('//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[2]/dd/span/text()').get()
        if moneys_test:
            moneys_test = int(''.join(moneys_test[:-4].split()))
        response_dict = {
            'okved': self.okved,
            'title': response.css('div.company-name::text').get().strip(),
            'ogrn': response.xpath('//*[@id="clip_ogrn"]/text()').get(),
            'okpo': int(response.css('#clip_okpo::text').get()),
            'status': response.css('div.company-status').attrib['class'].split()[-1],
            'regdate': ''.join(response.xpath('//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd/text()').get().split('.')[::-1]),
            'moneys': moneys_test,
            }
        yield response_dict
