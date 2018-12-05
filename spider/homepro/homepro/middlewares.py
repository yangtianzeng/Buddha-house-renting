# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class HomeproSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HomeproDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return 3

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import random
class RandomUADownloaderMiddleware(object):
    # 构造方法中定义一批ua列表
    def __init__(self):
        self.ua_list = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        ]

    # 发送请求之前会调用这个方法
    def process_request(self, request, spider):
        # 在这个方法中定制请求头
        ua = random.choice(self.ua_list)
        # 打印随机ua
        # print('*' * 100)
        # print(ua)
        # print('*' * 100)
        request.headers.setdefault('User-Agent', ua)
        # request.headers['User-Agent'] = ua


class ProxyDownloaderMiddleware(object):
    def __init__(self):
        self.ip_pool = self.get_ip()

    def get_ip(self):
        return [
            '222.170.0.102:53281',
            '118.212.95.34:53281',
            '101.37.79.125:3128',
            '112.250.109.173:53281',
            '113.200.56.13:8010',
            '59.46.44.6:9999',
            '111.198.154.116:8888',
            '60.191.201.38:45461',
            '180.119.65.175:3128',
            '171.221.239.11:808',
            '202.112.237.102:3128',
            '58.53.128.83:3128',
            '121.33.220.158:808',
            '218.60.8.83:3129',
            '61.128.208.94:3128',
            '61.128.208.94:3128',
            '124.42.68.152:90',
            '115.221.121.111:8010',
            '182.61.170.45:3128',
            '106.14.214.94:8118',
            '61.160.247.63:808',
            '218.60.8.99:3129',
            '203.86.26.9:3128',
        ]

    def process_request(self, request, spider):
        # 随机一个代理
        self.ip = random.choice(self.ip_pool)
        # print('#' * 100)
        # print('现在使用的代理是--%s--' % self.ip)
        # print('#' * 100)
        request.meta['proxy'] = 'http://' + self.ip
        request.meta['download_timeout'] = 5

    # 代理服务器链接失败，抛出异常，就会走这里
    def process_exception(self, request, exception, spider):
        # 干掉这个不可用的代理
        # self.ip_pool.remove(self.ip)
        if len(self.ip_pool) < 2:
            self.ip_pool = self.get_ip()
        # 请求需要重写发送
        return request