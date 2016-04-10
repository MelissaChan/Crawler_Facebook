# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-8 下午8:45

# import urllib
# import urllib2
# import cookielib
# import re

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()



# url = 'https://www.facebook.com/login'
# values = {'lsd':'AVoyJPy6','display':'','enable_profile_selector':'','isprivate':'','legacy_return':'1','profile_selector_ids':'','skip_api_login':'','signed_next':'','trynum':'1','timezone':'-480','lgndim':'eyJ3IjoxNjgwLCJoIjoxMDUwLCJhdyI6MTYxNSwiYWgiOjEwMjYsImMiOjI0fQ%3D%3D','lgnrnd':'213327_BGJT','lgnjs':'1460176408','email':'13918162228','pass':'720312xy','default_persistent':'0','qsstamp':'W1tbMCw2LDksMTMsMTcsMjEsMjgsMzAsNTAsNzIsODYsMTA2LDEwOSwxMjksMTU4LDIzMiwyMzQsMjQ1LDI0NywyNTAsMjY0LDI2NiwyNzAsMjg3LDI4OSwzMDIsMzI4LDMzNSwzNDgsMzczLDM3OSw0MzYsNDUyLDQ1OCw0NTksNDYzLDUxMyw1MTQsNTM2LDU0NCw2MDksNjUxXV0sIkFabTBma3lvVXBBQ0ZDNW9UcXV2VWh6c2Z3V3VMdDFNLW9MR01oY1Fqa0RkX1dxSURXblpvVVpEc1l5WjVYbHozTjBjNUJ1V1hzYnhvRzhOWnFRVVNhLTBPN3NCbzd0OEF2YjBGQi1XRjVRWjVhTDROa0Z6dGloUFM5RGhYWGVCbWM4OTlmbG9iQ0JfelZpRVBwZE5oeVQ5S0NmV1hPOHZKODk5MEVOMXJISzk4Ym0xVVRqNzJIQU9NTlowLVRpWDktWm9XVG14d0F0RHFFVmlqMDlta21ocUlPSU9Rd3NwVTVoczhlWUpQQ1ZyZm45S3Zxa0lkTU9lcmRMNFo1SmxVNE1ENGhfZUs1QXdVN2ZVUXFZYURON2tEczJHNmk1dGJqdTFMd2V1OXVWWWt3Il0%3D'}
# user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
# cookie = 'datr=r6kHV5j35EjuD7OOFmurq_bC; sb=5qkHV9U_7R5awAuYMq-RCW5G; locale=en_US; fr=0028b70rwtzaaQNx4.AWWvSzW0WRk_y5Fa201IgrNy9eA.BXB6oL.ea.AAA.0.AWWaUsWd; lu=RASITetWBeloDkb4jOALLZyQ; reg_fb_ref=https%3A%2F%2Fwww.facebook.com%2F%3Fstype%3Dlo%26jlou%3DAfeqK_691C6X2BLYiz4CJINX3nTcB-L0et4kS-bF1u01oYrY8Yd8XmUcSvbKtjLrMyL7G9D_V6Vg4_LiZmzy1kwExJZMiyRfQaEPNbpNCsOvcQ%26smuh%3D38789%26lh%3DAc_i0gNXLl3T0rjm; reg_fb_gate=https%3A%2F%2Fwww.facebook.com%2F%3Fstype%3Dlo%26jlou%3DAfeqK_691C6X2BLYiz4CJINX3nTcB-L0et4kS-bF1u01oYrY8Yd8XmUcSvbKtjLrMyL7G9D_V6Vg4_LiZmzy1kwExJZMiyRfQaEPNbpNCsOvcQ%26smuh%3D38789%26lh%3DAc_i0gNXLl3T0rjm; wd=1615x485'
# headers = {'User-Agent':user_agent,'Referer':'https://www.facebook.com/login'}
# data = urllib.urlencode(values)
# request =  urllib2.Request(url,data,headers)
# try:
#     response = urllib2.urlopen(request)
#     page = request.read()
# except urllib2.URLError,e:
#     print e.reason


# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#     'stuid':'201200131012',
#     'pwd':'23342321'
# })
# #登录教务系统的URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()

# page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
#
# try:
#     request = urllib2.Request(url,headers = headers)
#     response = urllib2.urlopen(request)
#     content = response.read().decode('utf-8')
#     pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>'
#                          '.*?<div class="content">(.*?)<!--.*?-->'
#                          '(.*?)<div class="stats">',re.S)
#     items = re.findall(pattern,content)
#     for item in items:
#         haveImg = re.search("img",item[2])
#         if not haveImg:
#             print item[0],item[1]
# except urllib2.URLError, e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason

# content = 'HuiHui is a girl~~~'
# fp = open('wenjian.txt','r')
# # fp.write(content)
# read = fp.readlines()
# for i in read:
#     print i.replace('\n','*')
# fp.close()



# from bs4 import BeautifulSoup
# import requests
# postload = {
#     'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
#     'EndStation':'60831846-f0e4-47f6-9b5b-46323ebdcef7',
#     'SearchDate':'2016/04/13',
#     'SearchTime':'09:30',
#     'SearchWay':'DepartureInMandarin'}
# res = requests.post('http://www.thsrc.com.tw/tw/TimeTable/SearchResult',data=postload)
# print res.text

# res = requests.get("http://www.qiushibaike.com/")
# soup = BeautifulSoup(res.text,"lxml")
# for item in soup.select('.mb15'):
#     print item.select('h2')[0].text.strip()
#     print item.select('.content')[0].text.strip()
#     print

# import requests
# import json
# token = 'CAACEdEose0cBADc5ZBD5kNGHIUZALbMYg8JgtOf29V4j32deCVnFiE7wJtZCPyxG4wFGmiEm5t4VHXEBswSZA8BKXoPgrfzAeMXq8ONxA1F0dIH3O76t3LeyCVZA6xcZB2dgamldqZCuIU2ORAuDGrFKRgIen2o74DA1whDsqtVgpadZCjk4J3FUoZA8XUfm08XkQZBOqOFuwq5AZDZD'
# res = requests.get('https://graph.facebook.com/v2.5/me?access_token=%s'%(token))
# print res.text
# jsondata = json.loads(res.text)
# print jsondata['summary']
# s = '\xe9\x9c\x80\xe8\xa6\x81 Cookie\xe6\x82\xa8\xe7\x9a\x84\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe6\x9c\xaa\xe5\x90\xaf\xe7\x94\xa8 Cookie\xe3\x80\x82\xe8\xaf\xb7\xe5\x9c\xa8\xe6\x82\xa8\xe7\x9a\x84\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe9\xa6\x96\xe9\x80\x89\xe9\xa1\xb9\xe4\xb8\xad\xe5\x90\xaf\xe7\x94\xa8 cookie \xe5\x90\x8e\xe7\xbb\xa7\xe7\xbb\xad\xe3\x80\x82'
# print s.decode('utf-8')


# Cookie使用
import urllib2
import cookielib
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener= urllib2.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print "Name = "+item.name
#     print "Value = "+item.value
filename = 'text_cookies.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)







