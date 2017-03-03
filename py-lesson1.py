# python第一节课，数组，元组，字典的切片，长度等，以及时间戳
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

a = {}
a['k1']=2.1
a['k2']=2.2
a['k4']=2.3
b = [1,2.1,'hello']

import time

a = int(time.time())

print a,type(a)

a = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(a))

print a

a = "2015-12-21 11-29-32"
a = int(time.mktime(time.strptime(a,"%Y-%m-%d %H-%M-%S")))
print a