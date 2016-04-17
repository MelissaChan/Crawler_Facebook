# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-8 下午8:45

import urllib
import urllib2
import cookielib
import requests

#####################################
# 模拟登录和自动获取cookie
# #登录的主页面
# hosturl = 'https://www.facebook.com/'
# #post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
# posturl = 'https://www.facebook.com/login.php?login_attempt=1&lwv=101'
#
# #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
# cj = cookielib.LWPCookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)
#
# #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
# h = urllib2.urlopen(hosturl)
#
# #构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
# headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36',
#            'referer' : 'https://www.facebook.com/login'}
# #构造Post数据，他也是从抓大的包里分析得出的。
# postData = {'lsd':'AVpOnApp',
#             'legacy_return':'1',
#             'trynum':'1',
#             'timezone':'-480',
#             'lgndim':'eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzAxLCJhaCI6NzQ0LCJjIjoyNH0=',
#             'lgnrnd':'194855_UBry',
#             'lgnjs':'1460342935',
#             'email':'13918162228',
#             'pass':'720312xy',
#             'persistent':'1',
#             'default_persistent':'1',
#             'qsstamp':'W1tbXV0sIkFabktXOWxpRnlUSExMTklJY3RjWEN4Qi03eHphUFYzV09mTXJkNFVIWlZFeXlSN1gxbVd0Vl81SVRZbVNwbnFOOXBMYnpiaG9kS1NBUzl1RGlqTWV5SVZucEo2Z2dUcmxfWDA4OVV1dTBOWEZRcU9sQ1ZTRW0tSFJIMWhLT3hmcjQ4WFdTQjNoaEh5WWxyWDhGbG1xZDdDQllRQkpvRmxDOWRxUFVOdEthb1VWQ0UwQVBDU2YwRHljYWJiNWVzenlIUnhrSjdTT3RwNWRXampSMHhmSzRKM0hEY3NVbm5WSk5MXzR2cDk5a1hRZ1EiXQ'
# }
#
# #需要给Post数据编码
# postData = urllib.urlencode(postData)
#
# #通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
# request = urllib2.Request(posturl, postData, headers)
# print request
# response = urllib2.urlopen(request)
# text = response.read()
# print text


##############################################
# cookie已知模拟登录
cookie = {"Cookie":'datr=MJkHV_pYgvXRkVrAX8iWyzDu; js_ver=2292; locale=en_US; pl=n; lu=gwyTTsGDzp6NEHc_yiR1ACoA; c_user=100009034522071; fr=08mYceA6qPKyWp9AX.AWUcP1ZJQOXx7SYC8KRyFHE0HNs.BXB5lC.4L.FcK.0.AWVaRCA8; xs=156%3AoHyObvMvRjpqqQ%3A2%3A1460536123%3A17302; csm=2; s=Aa61BlJ2zXlT5F7P.BXDgM8; sb=QpkHV9NVHcpmOSnCXWfwRKDt; act=1460864143313%2F17; p=-2; presence=EDvF3EtimeF1460864717EuserFA21B09034522071A2EstateFDt2F_5b_5dElm2FnullEuct2F1460861948BEtrFA2loadA2EtwF3892066209EatF1460864714122G460864717143CEchFDp_5f1B09034522071F5CC; wd=859x965'}
# html = requests.get('https://www.facebook.com/profile.php?id=100010109880950%3Fsection%3Drelationship&sk=about&section=relationship&pnref=about', cookies=cookie).content
# fp = open("facebook.html",'w')
# fp.write(html)
# fp.close()
# print html

#############################################
# bf4使用
import requests
import re
from bs4 import BeautifulSoup
res = requests.get("https://www.facebook.com/anthony.bell.7545",cookies = cookie).text
# res = requests.get("lineSectionPagelet?dpr=1&ajaxpipe=1&ajaxpipe_token=AXiJkyBFS00QEoR1&no_script_path=1&data=%7B%22profile_id%22%3A100009935435495%2C%22start%22%3A694252800%2C%22end%22%3A725875199%2C%22query_type%22%3A8%2C%22is_last_section%22%3Atrue%2C%22section_pagelet_id%22%3A%22pagelet_timeline_year_1992%22%2C%22parent_key%22%3Anull%2C%22force_no_friend_activity%22%3Afalse%7D&__user=100009034522071&__a=1&__dyn=aKhoFeyfyBm985A9UoHbgWC5ECiq2W8GA8Ay8VFLFwxBxCbzEeAq68K5U4e8wwG3Ou5R88wPGieKcDKuEjK5okDWxW3uiuumm2uVEOmFEW58nUOfz8gCxm5ErwwBK&__req=jsonp_7&__be=0&__pc=EXP1%3ADEFAULT&__rev=2288795&__adt=7",cookies = cookie).text
# soup = BeautifulSoup(res,"lxml")
# status = soup.select('p')
# <div class="_vb- _50f5">Single</div>

# pattern = re.compile('.*?<p>(.*?)</p>.*?')
# status = pattern.findall(res)
# print status
# for item in soup.select('.item'):
#     print item.select('xxx')[0].text.strip()

#############################################
# graph api + jason
# import json
# token = 'CAACEdEose0cBAH1WffZAOjz6XMnLN4h0aGwClSakfJi1Tg5fEtuplfOr09iKOCktQaILZAoCiMknaLwsc9D7ZAYPCS5fAjqlmP0ONKm6GZC4T3HlX4bmp94OzcgEdCz3o4AKKDhbOXWC5TcatBQZBzyASb51NSbwc8z5dDKBxTNJ2UHulhUtTPcDKZCkrm04C1Xwaz1DDvifWkcPdpDeDS'
# # res = requests.get('https://graph.facebook.com/v2.6/me?access_token=%s'%(token))
# res = requests.get('https://graph.facebook.com/100009079767777/me?access_token=%s'%(token))
# jsondata = json.loads(res)
# print jsondata
# # for name in jsondata['name']:
# #     print name

################Text Zone###################
# postData = {'__a':'1',
#             '__dyn':'5V5yAW8-aFoAwmgDxyIGzGomyrhEK5EK8GAFp8yeqrWo8ponUDAyoS2N6y8-bxu13wFG3J1Zi28rxvgjKcQiVWxeUlxicxmta3iinDBBzopK4Vq-EW5omUsz8gCxm5Erwwyo',
#             '__pc':'EXP1:DEFAULT',
#             '__req':'2v',
#             '__rev':'2276891',
#             '__user':'100009034522071',
#             'fb_dtsg':'AQGzW4WWKWmb:AQGz3aJ17eyl',
#             'ph':'V3',
#             'q':'[{"user":"100009034522071","page_id":"8bchw3","posts":[["timeline_feed_tracking",{"ft":{"top_level_post_id":"1711017372521428","tl_objid":"1711017372521428","fbfeed_location":10,"thid":"100008395452333:306061129499414:2:0:1462085999:-3007705617298354541"},"log_type":"impression"},1460379777008,0],["logger:CommentsTimeSpentLoggerConfig",{"viewer_has_interacted":false,"ordering_mode":"toplevel","post_fbid":"1711061259183706","start_time":1460379776,"end_time":1460379808,"time_spent_id":"8bchw3"},1460379808843,0],["timeline_feed_tracking",{"ft":{"top_level_post_id":"1710191805937318","tl_objid":"1710191805937318","fbfeed_location":10,"thid":"100008395452333:306061129499414:2:0:1462085999:-2835447812846245412"},"log_type":"impression"},1460379809916,0],["logger:CommentsTimeSpentLoggerConfig",{"viewer_has_interacted":false,"ordering_mode":"toplevel","post_fbid":"1711017372521428","start_time":1460379808,"end_time":1460379814,"time_spent_id":"8bchw3"},1460379814035,0],["timeline_feed_tracking",{"ft":{"top_level_post_id":"1710191675937331","tl_objid":"1710191675937331","fbfeed_location":10,"thid":"100008395452333:306061129499414:2:0:1462085999:-6133395718259613085"},"log_type":"impression"},1460379815849,0],["timeline_feed_tracking",{"ft":{"top_level_post_id":"1708412946115204","tl_objid":"1708412946115204","fbfeed_location":10,"thid":"100008395452333:306061129499414:2:0:1462085999:573687295468384833"},"log_type":"impression"},1460379816965,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"feedback_like_subscribe","event":"subscribe"},1460379818529,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_create_subscribe","event":"subscribe"},1460379818532,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_like_subscribe","event":"subscribe"},1460379818532,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"feedback_like_subscribe","event":"subscribe"},1460379818540,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_create_subscribe","event":"subscribe"},1460379818540,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_like_subscribe","event":"subscribe"},1460379818541,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"feedback_like_subscribe","event":"subscribe"},1460379818546,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_create_subscribe","event":"subscribe"},1460379818546,0],["logger:GraphQLSubscriptionsLoggerConfig",{"mechanism":"skywalker","subscription_call":"comment_like_subscribe","event":"subscribe"},1460379818547,0]],"trigger":"timeline_feed_tracking"}]',
#             'ts':'1460379837014',
#             'ttstamp':'265817112287528787758710998586581711225197744955101121108'
#             }
# headers = {"Cookie":'datr=r6kHV5j35EjuD7OOFmurq_bC; sb=5qkHV9U_7R5awAuYMq-RCW5G; locale=en_US; fr=0028b70rwtzaaQNx4.AWUiTSIeA4bQApij1UPQPY_NLnY.BXB6oL.ea.FcL.0.AWW9KeAG; lu=Tw_izfiIY8K7JPNOy6cRBQ6Q; c_user=100009034522071; xs=173%3APqmr7PknCdyiUw%3A2%3A1460375475%3A17302; csm=2; s=Aa7IIPHGI1mXPOe9.BXC4-0; pl=n; p=-2; act=1460378039355%2F14; presence=EDvF3EtimeF1460379829EuserFA21B09034522071A2EstateFDt2F_5b_5dElm2FnullEuct2F1460374876BEtrFA2loadA2EtwF3535362154EatF1460379821734G460379829200CEchFDp_5f1B09034522071F39CC; wd=1615x151'}
# postData = '=%7B%22subscriptions%22%3A[%7B%22topic%22%3A%22gqls%2Ffeedback_like_subscribe%2Ffeedback_id_1708412946115204%22%2C%22state%22%3A%22s%22%2C%22context%22%3A%7B%22transformContext%22%3A%22%7B%5C%22viewerID%5C%22%3A%5C%22100009034522071%5C%22%2C%5C%22appID%5C%22%3A155160167952447%2C%5C%22locale%5C%22%3A%5C%22en_US%5C%22%2C%5C%22queryID%5C%22%3A%5C%221710550255834803%5C%22%2C%5C%22serializedQueryParameters%5C%22%3A%5C%22%7B%5C%5C%5C%22input%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22client_subscription_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22809f0b50-80a4-4feb-917d-72d66991bd22%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22feedback_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%221708412946115204%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%7D%5C%22%7D%22%2C%22locale%22%3A%22en_US%22%7D%7D]%7D'
# html = requests.post('https://www.facebook.com/profile.php?id=100008395452333&pnref=story',postData)
# html2 = requests.get('https://www.facebook.com/profile.php?id=100008395452333',cookies=headers)
# print html2.text
# fp = open("facebook.html",'w')
# fp.write(html2.text)
# fp.close()












