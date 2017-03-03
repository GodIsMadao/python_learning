# -*- coding: utf-8 -*-
# class Student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score

# 	def get_student(self):
# 		print '%s:%s'%(self.name,self.score)

# 	def get_grade(self):
# 		if self.score>=90:
# 			print 'A'
# 		elif self.score>=60:
# 			print 'B'
# 		else:
# 			print 'C'
# bart=Student('Bart',66)
# bart.get_student()
# bart.get_grade()
# class Student(object):
# 	__slots__=('name','age')
# 	def set_age(self, age): # 定义一个函数作为实例方法
# 	    self.age = age

# s = Student()
# s.name='Micro'
# s.age=10
# s.score=99

# @property
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value , int):
			raise ValueError('score must be Integer')
		if value<0 or value > 100:
			raise ValueError('score must between 0 and 100')
		self._score=value

s = Student()
s.score = 999
print s.score