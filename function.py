# -*- coding: utf-8 -*-
# import os
# print [d for d in os.listdir('.')]
d = {'x':'A','y':'B','z':'C'}
print [k+'='+v for k,v in d.iteritems()]
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
g = (x*x for x in xrange(10))
# print g.next()
# for n in g:
# 	print n

def fab(max):
	n,a,b=0,0,1
	while n<max:
		print b
		a,b=b,a+b
		n+=1

fab(9)