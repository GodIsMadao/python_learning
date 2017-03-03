# -*- coding: utf-8 -*-

# print(int('123213',base=16))
# base 参数是进制转换
# import functools
# int2 = functools.partial(int,base = 2)
# print(int2("0000111111"))

#Python里*args 与 **kwargs的用法
#当函数参数不确定时，使用*args与**kwargs,*args有key值，**kwargs没有key值
def fun_var_args(farg, *args): 
    print "arg:", farg 
    for value in args: 
        print "another arg:", value 
 
fun_var_args(1, "two", 3) # *args可以当作可容纳多个变量组成的list 

def fun_var_kwargs(farg,**kwargs):
	print "arg:",farg
	for item in kwargs:
		print "another arg's value:",item.value,"another arg's key",item.key
fun_var_kwargs(farg=1, myarg2="two", myarg3=3)