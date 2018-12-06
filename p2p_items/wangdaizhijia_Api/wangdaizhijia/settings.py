# -*- coding: utf-8 -*-

# Scrapy settings for wangdaizhijia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangdaizhijia'

SPIDER_MODULES = ['wangdaizhijia.spiders']
NEWSPIDER_MODULE = 'wangdaizhijia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wangdaizhijia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#'Accept-Encoding':'gzip, deflate, br',
#'Accept-Language':'zh-CN,zh;q=0.9',
#'Cache-Control':'max-age=0',
#'Connection':'keep-alive',
#'Cookie':'__jsluid=4f99f81c1028512ec0ef4a12af17a730; route=ad03ba7dbd66044dc92b523e205be8ad; TY_SESSION_ID=8b615695-6c6a-4d7d-a361-a2cb26f33e13; advidadv_in-0=0; _ga=GA1.2.1761670801.1520048568; _gid=GA1.2.1420990960.1520048568; gr_user_id=c83681df-d1b1-4163-943d-0efd549b2d0c; gr_session_id_1931ea22324b4036a653ff1d3a0b4693=8e1dcaba-b232-41f9-bef0-91f389b391f8; Hm_lvt_9e837711961994d9830dcd3f4b45f0b3=1520048568; Hm_lpvt_9e837711961994d9830dcd3f4b45f0b3=1520048568; UM_distinctid=161e9f478d8b15-0e3b182294316b-3b60450b-1fa400-161e9f478d9870; CNZZDATA5008302=cnzz_eid%3D879998123-1520044847-%26ntime%3D1520044847; _pk_id.1.b30f=62646025c5ba912b.1520048569.1.1520048569.1520048569.; _pk_ses.1.b30f=*; WDZJptlbs=1',
'Host':'shuju.wdzj.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wangdaizhijia.middlewares.WangdaizhijiaSpiderMiddleware': 543,
#}
#
# FEED_URI = 'c://User//99329//b.csv'
# FEED_FORMAT = 'csv' #csv小写

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'wangdaizhijia.middlewares.WangdaizhijiaDownloaderMiddleware': 200,
   'wangdaizhijia.middlewares.WangdaizhijiaSpiderMiddleware': 200,   #下载中间键中添加ip代理
   #'wangdaizhijia.Rotate_useragent.RotateUserAgentMiddleware': 301,
   'wangdaizhijia.RandomUserAgentMiddleware.RandomUserAgentMiddleware': 300,  #useragent请求头
   #'wangdaizhijia.pipelines.WangdaizhijiaPipeline': 400,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':100
}

RETRY_ENABLE=False

#DOWNLOAD_DELAY = 3
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'wangdaizhijia.pipelines.WangdaizhijiaPipeline': 301,
# }

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


#
# IPPOOL=[
#     {"ipaddr":"192.168.0.100"},  #自己的ip也不行
#     # {"ipaddr":"61.152.81.193:9100"},
#     # {"ipaddr":"120.204.85.29:3128"},
#     # {"ipaddr":"219.228.126.86:8123"},
#     # {"ipaddr":"61.152.81.193:9100"},
#     # {"ipaddr":"218.82.33.225:53853"},
#     # {"ipaddr":"223.167.190.17:42789"}
# ]
#

