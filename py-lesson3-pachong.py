#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 15:12:24
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup
# GET 方法
# url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

# request = urllib2.Request(url=url)
# response = urllib2.urlopen(request,timeout=20)
# result = response.read()

# POST方法
url = 'http://shuju.wdzj.com/depth-data.html'
data = urllib.urlencode({'type1': 1, 'type2': 2, 'status': 0, 'wdzjPlatId': 59})
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request,data)
result = response.read()

# print result
# 把json字符串转成字典:json.loads()
for key in json.loads(result).keys():
	print key