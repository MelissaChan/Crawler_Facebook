# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-8 下午8:45

import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()
