from scrapy import cmdline
name = 'kuaidi100_spider'
cmd = 'scrapy crawl {}  '.format(name)
cmdline.execute(cmd.split())









