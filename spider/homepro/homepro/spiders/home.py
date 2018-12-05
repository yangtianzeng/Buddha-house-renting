# -*- coding: utf-8 -*-
import scrapy
from homepro.items import HomeproItem
import re
class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['zu.fang.com']
    start_urls = ['http://zu.fang.com/cities.aspx']

    def parse(self, response):
        hrefs = response.xpath('//div[@class="onCont"]/ul/li/a/@href').extract()
        for href in hrefs:
            href = 'http:'+ href
            yield scrapy.Request(url=href,callback=self.parse_city,dont_filter=True)


    def parse_city(self, response):
        page_num = response.xpath('//div[@id="rentid_D10_01"]/span[@class="txt"]/text()').extract()[0].strip('共页')
        # print('*' * 100)
        # print(page_num)
        # print(response.url)

        for page in range(1, int(page_num)):
            if page == 1:
                url = response.url
            else:
                url = response.url + 'house/i%d' % (page + 30)
            yield scrapy.Request(url=url, callback=self.parse_hrefinfo, dont_filter=True)

    def parse_hrefinfo(self, response):
        #http://zu.fang.com
        urls = (response.url).split('/house')[0]
        url = urls.rstrip('/')
        hrefs = response.xpath('//p[@class="title"]/a/@href').extract()
        for link in hrefs:
            href = url + link
            print(href)
            yield scrapy.Request(url=href, callback=self.parse_houseinfo, dont_filter=True)


    def parse_houseinfo(self,response):
        try:
            city = response.xpath('//div[contains(@class,"bread")]/a[2]/text()').extract()[0][:-2]
            title = response.xpath('//h1/text()').extract()[0]
            price = response.xpath('//div[contains(@class,"trl-item sty1")]/i/text()').extract()[0]
            paytype = response.xpath('//div[contains(@class,"trl-item sty1")]/text()').extract()[-1].strip('\r\n ')
            renttype = response.xpath('//div[@class="tt"]/text()').extract()[0]
            hometype = response.xpath('//div[@class="tt"]/text()').extract()[1]
            decorade = response.xpath('//div[@class="tt"]/text()').extract()[-1]
            info = response.xpath('//div[contains(@class,"rcont")]//text()').extract()
            str = "".join(i for i in info)
            p1 = re.compile(r'[(](.*?)[/)]', re.S)
            region = re.findall(p1, str)[0]
            address = response.xpath('//div[contains(@class,"lab")][contains(text(),"地")]//following-sibling::div[1]//text()').extract()[0]
        except Exception as e:
            address = "暂无信息"
        try:
            area = response.xpath('//div[@class="tt"]/text()').extract()[2]
        except Exception as e:
            area = "暂无"

        try:
            linkman = response.xpath('//span[contains(@class,"zf_jjname")]/a/text()')[-1].extract()
            phone = response.xpath('//div[@class="tjcont-list-cline2 tjcont_gs clearfix"]/p/text()').extract()[0]
        except Exception as e:
            linkman = "暂无"
            phone = "暂无"

        try:
            img = 'http:' + response.xpath('//div[@class="bigImg"]/img[1]/@src').extract()[0]
        except Exception as e:
            img = "暂无图片展示"

        try:
            lights = response.xpath('//div[contains(@class,"fyms_con floatl gray3")]/text()').extract()
            features = '#'.join(i for i in lights)
        except Exception as e:
            features = "暂无描述"

        item = HomeproItem()
        for field in item.fields.keys():
            item[field] = eval(field)
        yield item









