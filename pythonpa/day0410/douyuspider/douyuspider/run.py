from scrapy import cmdline

name = 'douyu'
cmd ='scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())