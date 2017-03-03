# -*- coding: utf-8 -*-
# @Date    : 2017年2月9日 13:03:11
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

fr = open("result.txt",'r')
fw = open("result.json",'w')

address = []
name = []
longitude = []
latitude = []

count = 0
for line in fr:
	line = line.strip()
	line = unicode(line)
	count = count +1
	# print line[line.rfind("地址："):line.rfind(" 经度")]
	old_name = line[line.rfind("名称:"):line.rfind(" 地址")].replace("名称:","")
	old_address = line[line.rfind("地址："):line.rfind(" 经度")].replace("地址：","")
	old_long = line[line.rfind("经度:"):line.rfind(" 维度")].replace("经度:","")
	old_lat = line[line.rfind("维度"):].replace("维度:","")
	# print count,old_lat
	name.append(old_name)
	address.append(old_address)
	longitude.append(old_long)
	latitude.append(old_lat)

str = '['
for x in xrange(0,92):
	str = str +"{\"name\":\""+name[x]+"\",\"address\":\""+address[x]+"\",\"longitude\":"+longitude[x]+",\"latitude\":"+latitude[x]+"},"

str = str[:-1]+"]"
fw.write(str)
fr.close()
fw.close()
# print str
# for line in name:
# 	print line
