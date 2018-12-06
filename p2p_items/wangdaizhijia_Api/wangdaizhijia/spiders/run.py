from scrapy import cmdline
name = 'wangdaizhijia_spider'
cmd = 'scrapy crawl {} -o 2.csv'.format(name)
cmdline.execute(cmd.split())
#www.shuju.wdzj.com/plat-info-659.html








