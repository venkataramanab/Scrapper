# Created by venkataramana on 06/11/18.
from scrapy import cmdline

cmdline.execute("scrapy crawl naukri -o samples/sample.json".split())
