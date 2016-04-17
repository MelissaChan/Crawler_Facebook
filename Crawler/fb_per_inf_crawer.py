# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-16 下午10:53

import requests
import Queue
import time
from parse import perInf

class FbPerInfCrawler(object):
    def __init__(self,root_url):
        # self.crawled_queue = crawled_queue()#类
        # self.crawling_queue = crawleing_queue()#类
        self.crawled_queue = Queue.Queue(0)#类
        self.crawling_queue = Queue.Queue(0)#类
        self.root_url = root_url

    def start(self):
        self._seed_url(self.root_url)#crawling_queue中已经保存了所有可以爬的数据
        while not self.crawling_queue.empty():#判断还有要爬的链接
            url = self.crawling_queue.get()
            print "正在爬爬爬",url[0],url[1]

            per_inf = perInf(url)#类
            data = per_inf.start()#start返回数据或空
            if data != None:
                self._write_mysql(data)#函数或类都可以
            self.crawled_queue.put(url)
        print '爬爬爬结束'

    def _write_mysql(self,data):
        mysql=

    def _seed_url(self,url):

        #进行解析得到urls并找到判断条件
        urls = ''
        if  (......):
            for url in urls:
                if not url in self.crawling_queue.queue:#避免重复
                    self.crawling_queue.put(url)
        else:
            for url in urls:
                self._seed_url(url)



if __name__ == '__main__':
    url = str(raw_input('input the root_url:'))
    crawler = FbPerInfCrawler(url)
    crawler.start()
