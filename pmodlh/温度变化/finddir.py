#找某路径下的"*.txt"文件
'''
运行脚本：run ploTemp.py
实例化类：aa=finddir('E:\\code\\python\\plotTemp\\2020.2\\')
运行函数：aa.returndir()
'''
import os
class finddir():
	def __init__(self,path):
		self.path=path
	def returndir(self):
		ld=[]
		dirs=os.listdir(self.path)
		for i in dirs:
			if os.path.splitext(i)[1]=='.txt':  #分开文件名和扩展名
				ld.append(i)
		return ld
