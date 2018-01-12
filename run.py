from scrapy import cmdline

name = 'zimuzu'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
