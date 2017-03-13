# -*- coding: utf-8 -*-
BOT_NAME = 'jobaware'

SPIDER_MODULES = ['jobaware.spiders']
NEWSPIDER_MODULE = 'jobaware.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'topic (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
    'scrapy.spidermiddleware.depth.DepthMiddleware': None,
    'scrapy.spidermiddleware.offsite.OffsiteMiddleware': None,
    'scrapy.spidermiddleware.referer.RefererMiddleware': None,
    'scrapy.spidermiddleware.urllength.UrlLengthMiddleware': None
}

DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
}

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'


HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
# REDIRECT_ENABLED = False # scrapy docs suggestion for broad crawls
COOKIES_ENABLED = False 
DOWNLOAD_TIMEOUT = 240
# DOWNLOAD_TIMEOUT = 15 # scrapy docs suggestion for broad crawls
RETRY_ENABLED = False 
DOWNLOAD_MAXSIZE = 1*1024*1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = False

# concurrency
CONCURRENT_REQUESTS = 64
# CONCURRENT_REQUESTS = 100 # scrapy docs suggestion for broad crawls
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.0

LOG_LEVEL = 'INFO' 

REACTOR_THREADPOOL_MAXSIZE = 32
# REACTOR_THREADPOOL_MAXSIZE = 20 # scrapy docs suggestion for broad crawls
DNS_TIMEOUT = 180

AJAXCRAWL_ENABLED = True 