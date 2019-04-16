from scrapy import cmdline

name = 'sun'
cmd ='scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())