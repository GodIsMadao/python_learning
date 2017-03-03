import sys
def test():
	arg = sys.argv
	if len(arg)==1:
		print 'hello world'
	elif len(arg)==2:
		print 'hello %s'%arg[1]
	else:
		print 'too many arguments'

if __name__=='__main__':
	test()