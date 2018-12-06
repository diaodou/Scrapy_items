from scrapy import cmdline

name = 'Zhimafen_spider2'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())