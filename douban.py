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

tag = []
url = 'https://movie.douban.com/j/search_tags?type=movie'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request,timeout=20)
result = json.loads(response.read())
tags = result['tags']

movies = []

for tag in tags:
	limit = 0
	while 1:
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' +tag + '&sort=recommend&page_limit=20&page_start=' + str(limit)
		request = urllib2.Request(url=url)
		response = urllib2.urlopen(request,timeout=20)
		result = json.loads(response.read())

		result = result['subjects']

		if len(result) == 0:
			break

		limit +=20

		for item in result:
			movies.append(item)
		break
	break

for x in xrange(0, len(movies)):
	item = movies[x]
	request = urllib2.Request(url = item['url'])
	response = urllib2.urlopen(request,timeout=20)
	result = response.read()
	html = BeautifulSoup(result)
	title = html.select('h1')[0]
	title = title.select('span')[0]
	title = title.get_text()
	print title
