import scrapy


class w3cSpider(scrapy.Spider):
    name = 'zimuzu'  # 爬虫名称，命令行运行时要用到
    allowed_domains = ['www.zimuzu.tv']
    start_urls = [
        'http://www.zimuzu.tv/article'  # 爬取的页面地址
    ]

    def parse(self, response):  # scrapy根据爬取地址发送请求后调用parse进行数据提取
        for xssss in response.selector.xpath('//a/text()').extract():
            print(xssss)
        for uri in response.xpath('//h3/a/@href').extract():
            url = response.urljoin(uri)
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.selector.xpath('//h2/text()').extract_first()
        print()
