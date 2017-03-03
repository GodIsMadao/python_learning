# -*- coding: utf-8 -*-
# @Date    : 2017年2月9日 13:03:11
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

fr = open('python1.txt','r')
fw = open('result.txt','w')
address = []
name = []
longitude = []
latitude = []


for line in fr:
	line = unicode(line)
	for x in xrange(0,len(line)):
		if(line[0:5]=='02-08'):
			# print line[0:59]
			line = line.replace(line[0:59],"")
	# print line
	fw.write(line)

	longitude.append(line[line.rfind("经度:"):line.rfind(" ")])	

	# 不必整齐格式，只需要取出'维度:'后10位 '经度:'后9位 '地址：'(中文冒号)后到空格位置 
	# '名称:'直到空格 每个空格做一次切片
# longitude.append(line[line.rfind("经度:"):line.rfind(" ")])
# 	count = 1
# for line in longitude:
# 	count = count + 1
# 	print count,line
#还是得整齐格式

fr.close()
fw.close()
