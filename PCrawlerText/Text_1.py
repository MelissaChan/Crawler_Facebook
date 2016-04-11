# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-8 下午8:45

import urllib
import urllib2
import cookielib

#登录的主页面
hosturl = 'https://www.facebook.com/'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'https://www.facebook.com/login.php?login_attempt=1&lwv=101'

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36',
           'referer' : 'https://www.facebook.com/login'}
#构造Post数据，他也是从抓大的包里分析得出的。
postData = {'lsd':'AVpOnApp',
            'legacy_return':'1',
            'trynum':'1',
            'timezone':'-480',
            'lgndim':'eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzAxLCJhaCI6NzQ0LCJjIjoyNH0=',
            'lgnrnd':'194855_UBry',
            'lgnjs':'1460342935',
            'email':'13918162228',
            'pass':'720312xy',
            'persistent':'1',
            'default_persistent':'1',
            'qsstamp':'W1tbXV0sIkFabktXOWxpRnlUSExMTklJY3RjWEN4Qi03eHphUFYzV09mTXJkNFVIWlZFeXlSN1gxbVd0Vl81SVRZbVNwbnFOOXBMYnpiaG9kS1NBUzl1RGlqTWV5SVZucEo2Z2dUcmxfWDA4OVV1dTBOWEZRcU9sQ1ZTRW0tSFJIMWhLT3hmcjQ4WFdTQjNoaEh5WWxyWDhGbG1xZDdDQllRQkpvRmxDOWRxUFVOdEthb1VWQ0UwQVBDU2YwRHljYWJiNWVzenlIUnhrSjdTT3RwNWRXampSMHhmSzRKM0hEY3NVbm5WSk5MXzR2cDk5a1hRZ1EiXQ'
}

#需要给Post数据编码
postData = urllib.urlencode(postData)

#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text




