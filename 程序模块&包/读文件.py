#例子
#read rms.dat

import numpy
class openfile:
	def __init__(self,title):
		self.title=title
	def readtxt(self):
		return numpy.loadtxt(self.title)

'''
f=openfile('rms.dat')
data=f.readtxt()
'''
