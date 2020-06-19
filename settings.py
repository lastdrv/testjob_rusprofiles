# -*- coding: utf-8 -*-

# Scrapy settings for testjob project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from random import choice


ITEM_PIPELINES = {'scrapy_mysql_pipeline.MySQLPipeline': 300}

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'lastdrv'
MYSQL_PASSWORD = '12345'
MYSQL_DB = 'db_test'
MYSQL_TABLE = 'tbl_test'
MYSQL_UPSERT = True

BOT_NAME = 'testjob'

SPIDER_MODULES = ['testjob.spiders']
NEWSPIDER_MODULE = 'testjob.spiders'

RETRY_TIMES = 5
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
  'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
  'scrapy_proxies.RandomProxy': 100,
  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

PROXY_SETTINGS = {
  # Proxy list containing entries like
  # http://host1:port
  # http://username:password@host2:port
  # http://host3:port
  # ...
  # if PROXY_SETTINGS[from_proxies_server] = True , proxy_list is server address (ref https://github.com/qiyeboy/IPProxyPool and https://github.com/awolfly9/IPProxyTool )
  # Only support http(ref https://github.com/qiyeboy/IPProxyPool#%E5%8F%82%E6%95%B0)
  # list : ['http://localhost:8000?protocol=0'],
  'list':['list_proxies.txt'],

  # disable proxy settings and  use real ip when all proxies are unusable
  'use_real_when_empty':False,
  'from_proxies_server':False,

  # If proxy mode is 2 uncomment this sentence :
  # 'custom_proxy': "http://host1:port",

  # Proxy mode
  # 0 = Every requests have different proxy
  # 1 = Take only one proxy from the list and assign it to every requests
  # 2 = Put a custom proxy to use in the settings
  'mode':0
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = {'User-Agent': choice(open('list_user_agents.txt').read().split('\n'))}
USER_AGENT = choice(open('list_user_agents.txt').read().split('\n'))

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'testjob.middlewares.TestjobSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'testjob.middlewares.TestjobDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'testjob.pipelines.TestjobPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
