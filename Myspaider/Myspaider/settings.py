# -*- coding: utf-8 -*-

# Scrapy settings for Myspaider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Myspaider'

SPIDER_MODULES = ['Myspaider.spiders']
NEWSPIDER_MODULE = 'Myspaider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Myspaider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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

USER_AGENT = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


ROBOTSTXT_OBEY = False #不遵守Robot协议
DOWNLOAD_DELAY = 3 #延迟
COOKIES_ENABLED = True #启用 cookie

HEADERS = {
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
}
META = {
	'dont_redirect': True,
	'handle_httpstatus_list': [301, 302]
}

COOKIES = {
	'user_trace_token':'20190424133640-665bada2-3c72-47c9-a09b-93d2d1abbb5b',
	'_ga':'GA1.2.1792683107.1556084204',
	'LGUID':'20190424133644-f21cab95-6652-11e9-9cdd-5254005c3644', 
	'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%2216a590e74be39c-09549845bff5e4-366e7e04-1296000-16a590e74bf89a%22%2C%22%24device_id%22%3A%2216a590e74be39c-09549845bff5e4-366e7e04-1296000-16a590e74bf89a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
	'index_location_city':'%E5%8C%97%E4%BA%AC',
	'JSESSIONID':'ABAAABAAAGGABCBCC8D1422BE6B6D0151BA30A5E43AD521',
	'_gid':'GA1.2.82560741.1558797744',
	'_gat':'1',
	'LGSID':'20190525232224-e61c6371-7f00-11e9-a708-525400f775ce',
	'PRE_UTM':'',
	'PRE_HOST':'www.google.com',
	'PRE_SITE':'https%3A%2F%2Fwww.google.com%2F',
	'PRE_LAND':'https%3A%2F%2Fwww.lagou.com%2F',
	'TG-TRACK-CODE':'index_navigation',
	'SEARCH_ID':'bfb47596db8148b68168f384d30dc15d',
	'X_HTTP_TOKEN':'f6050caae1c3a34e757797855115fe95ca491f976b',
	'LGRID':'20190525232241-f01f0f84-7f00-11e9-a708-525400f775ce',
	'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1557884048,1558416036,1558797744,1558797761',
	'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1558797761'
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Myspaider.middlewares.MyspaiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Myspaider.middlewares.MyspaiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Myspaider.pipelines.MyspaiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
