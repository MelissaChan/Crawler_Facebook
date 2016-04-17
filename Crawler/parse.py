# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-16 下午10:53

from per_data import Inf
from bs4 import BeautifulSoup
import requests
import re

class perInf(object):

    def __init__(self,url):
        self.url = url
        self.data = Inf()
        self.time = '0001.01.01'
        self.cookie = {"Cookie":'datr=MJkHV_pYgvXRkVrAX8iWyzDu; js_ver=2292; locale=en_US; pl=n; lu=gwyTTsGDzp6NEHc_yiR1ACoA; c_user=100009034522071; fr=08mYceA6qPKyWp9AX.AWUcP1ZJQOXx7SYC8KRyFHE0HNs.BXB5lC.4L.FcK.0.AWVaRCA8; xs=156%3AoHyObvMvRjpqqQ%3A2%3A1460536123%3A17302; csm=2; s=Aa61BlJ2zXlT5F7P.BXDgM8; sb=QpkHV9NVHcpmOSnCXWfwRKDt; act=1460864143313%2F17; p=-2; presence=EDvF3EtimeF1460864717EuserFA21B09034522071A2EstateFDt2F_5b_5dElm2FnullEuct2F1460861948BEtrFA2loadA2EtwF3892066209EatF1460864714122G460864717143CEchFDp_5f1B09034522071F5CC; wd=859x965'}

    def start(self):
        self._get_status_inf()
        return self.data
    #######################################

    def _get_status_inf(self):
        #解析网页得状态
        status = ''
        self.time = ''
        valueStatus = ['Married','In a relationship','Engaged','In a domestic partnership','It\'s complicated','In an open relationship','In a civil union']
        try:
            status_url = self.url+'/about?section=relationship&pnref=about'
            gender_url = self.url+'/&sk=about&section=contact-info&pnref=about'
            res = requests.get(status_url,cookies = self.cookie)
            soup = BeautifulSoup(res)
            status = soup.select('._50f3')
            isValue = False
            if status in valueStatus:
                isValue = True
            if isValue == True:#需要爬的人
                self.data.id =
                self.data.gender =
                self.data.partner_id =
                self.data.name =
                self.data.status = status
                self.data.date = self.time
                self._get_first_page()
                if time_url == None:
                    return None
                else:
                    return self._get_data(time_url)
            else :
                return None
        except Exception,e:
            print '找Status出错了，呜呜呜'
            print Exception,":",e
    def _get_first_page(self):
        res = requests.get(self.url,cookies = self.cookie)
        #得到第一个ajax参数，
        ajax = ''
        _



    def _start_time(self,url):
        #解析网页得到时间得到下一次的网址
        try:
            res = requests.get(url= url,cookies = self.cookie).text
            soup = BeautifulSoup(res)
            time = soup.select()

            if self.time<=self.time-sangeyue:
                return

            next_url = ''


            if self.time-sangeyue<=time <=self.time ':#一个范围
                 _get_data(res)

                return url
            else:
                self._start_time(next_url)
            return None
        except Exception,e:
            print '没能得到下一个网址'
            print Exception,":",e

    def _get_data(self,res):
        #解析数据得到url,data和time
        try:
            soup = BeautifulSoup(res)
            id = soup.select()
            name = soup.select()
            gender= soup.select()
            partnerId = soup.select()
            status = soup.select()
            date = soup.select()
            interaction = soup.select()
            self.data.append(id,name,gender,partnerId,status,date,interaction)
        except Exception,e:
            print '解析数据挂了～～'
            print Exception,":",e

