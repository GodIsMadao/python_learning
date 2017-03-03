#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-21 14:36:08

import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

fr = open('xyj.txt','r')

charcter = []
stat = {}

for line in fr:
	line = line.strip()

	if len(line) == 0:
		continue

	line = unicode(line)
	for x in xrange(0, len(line)):
		if line[x] in ['\t','\n','“','',' ','[',']','(',')','《','》','？','{','}','，','。','（','）','：','！']:
			continue

		if not line[x] in charcter:
			charcter.append(line[x])

		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		stat[line[x]] += 1

fw = open('result.json','w')
fw.write(json.dumps(stat))
fw.close()

stat =  sorted(stat.iteritems(),key = lambda d:d[1],reverse=True)


# 可能是有不同输入法带来的空格不同

for x in xrange(0,20):
	print stat[x][0],stat[x][1]

fw = open('result.csv','w')
for item in stat:
	fw.write(item[0] + ',' + str(item[1]) + '\n')

fw.close()

fr.close()