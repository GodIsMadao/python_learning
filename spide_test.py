#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-18 18:10:58
# @Author  : Your Name (you@example.org)
# @Version : $id$

# python简单爬取网上图片
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	image = re.compile(reg)
	imglist = re.findall(image,html)
	x = 0
	for imgurl in imglist:
		x+=1
		urllib.urlretrieve(imgurl,'%s.jpg' % x)

html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)




