#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-18 18:10:58
# @Author  : Your Name (you@example.org)
# @Version : $id$

# python简单爬虫
import urllib
# import json
import re
import basesoup

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getData(html):
	reg = r''

# html = getHtml('你要放的URL')
html = getHtml('http://localhost:8080/test.json')

print(html)