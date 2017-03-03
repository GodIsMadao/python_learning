#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-29 09:46:58
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# yahoo test
import urllib2
import urllib

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
request = urllib2.Request(url=url)
response = urllib2.urlopen(request,timeout=20)
result = response.read()
print result
# resp=request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# resp_text = resp.read()
# print resp_text





