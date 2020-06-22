from random import choice


MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'lastdrv'
MYSQL_PASSWORD = '12345'
MYSQL_DB = 'db_test'
MYSQL_TABLE = 'tbl_test'
MYSQL_UPSERT = True
#FEED_EXPORT_ENCODING = 'utf-8'

#ROTATING_PROXY_LIST = []
ROTATING_PROXY_LIST_PATH = 'list_proxies.txt'

# Количество конкурирующих запросов
CONCURRENT_REQUESTS = 5

# Ожидание таймаута в секундах
DOWNLOAD_TIMEOUT = 10


# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = choice(open('list_user_agents.txt').read().split('\n'))

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

#RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 3
#RANDOM_UA_PER_PROXY = True

ROTATING_PROXY_CLOSE_SPIDER = True
ROTATING_PROXY_PAGE_RETRY_TIMES = 30
ROTATING_PROXY_BACKOFF_BASE = 3000

BOT_NAME = 'testjob'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ITEM_PIPELINES = {'scrapy_mysql_pipeline.MySQLPipeline': 300}

#SPIDER_MIDDLEWARES = {
#    'rotating_proxies.middlewares.CustomSpiderMiddleware': 543
#}