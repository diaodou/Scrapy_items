from scrapy import cmdline
name  ='lianjia_spider'
cmd = 'scrapy crawl {} -o 2.csv'.format(name)
cmdline.execute(cmd.split())
