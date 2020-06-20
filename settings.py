from random import choice


MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'lastdrv'
MYSQL_PASSWORD = '12345'
MYSQL_DB = 'db_test'
MYSQL_TABLE = 'tbl_test'
MYSQL_UPSERT = True

#ROTATING_PROXY_LIST = []
ROTATING_PROXY_LIST_PATH = 'list_proxies.txt'

# Количество конкурирующих запросов
CONCURRENT_REQUESTS = 5

# Задержка между загрузками в секундах
DOWNLOAD_DELAY = 10

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = choice(open('list_user_agents.txt').read().split('\n'))

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ROTATING_PROXY_CLOSE_SPIDER = True
ROTATING_PROXY_PAGE_RETRY_TIMES = 0
ROTATING_PROXY_BACKOFF_BASE = 3000

BOT_NAME = 'testjob'

SPIDER_MODULES = ['testjob.spiders']
NEWSPIDER_MODULE = 'testjob.spiders'

ITEM_PIPELINES = {'scrapy_mysql_pipeline.MySQLPipeline': 300}
