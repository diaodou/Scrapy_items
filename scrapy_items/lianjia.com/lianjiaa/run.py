from scrapy import cmdline
name = 'lianjiaa_spider'
cmd = 'scrapy crawl {} -o 1.csv '.format(name)
cmdline.execute(cmd.split())





