#简单读取文件数据，返回数组型
#read rms.dat

import numpy

def readtxt(filename):
	data=numpy.loadtxt('test.txt', dtype=int, delimiter=' ') #dtype字符型；delimiter分隔符
	return data

data=readtxt('test.txt')
