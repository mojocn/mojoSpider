import scrapy
from scrapy.selector import  Selector
from myScrapy.items import W3CItem
class w3cSpider(scrapy.Spider):
    name='w3c_spider'#爬虫名称，命令行运行时要用到
    allowed_domains=['w3school.com.cn']
    start_urls=[
        '<a href="http://www.w3school.com.cn/xml/xml_syntax.asp">w3school>'#爬取的页面地址
    ]
    def parse(self, response):#scrapy根据爬取地址发送请求后调用parse进行数据提取
        sel=Selector(response)
        sites=sel.xpath('//div[@id="course"]/ul/li')#使用xpath提取页面信息
        for site in sites:
            item = W3CItem()
            title = site.xpath('a/@title').extract()#提取title
            link = site.xpath('a/@href').extract()#提取链接
            desc=site.xpath('a/text()').extract()#提取描述
            item['title']=title[0]#组织item数据
            item['link']=link[0]
            item['desc']=desc[0]
            yield  item #返回item数据给pipeline使用