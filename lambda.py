# print(list(map(lambda x:x*x,[1,3,4,5,6,7,8,8])))
# f = lambda x : x*x
# print(f)
# # function <lambda> at 0x0000000002A403C8
# # 16^16-1
def log(func):
	def wrapper(*arg,**kw):
		print('call %s():' %func.__name__)
		return func(*arg,**kw)
	return wrapper

@log
def now():
	print ('2016-2-14')

now()