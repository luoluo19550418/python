#purpose：找某路径下的"*.txt"文件
'''步骤：
运行脚本：run finddir.py
实例化类：aa=FindDir('E:\\code\\python\\plotTemp\\2020.2\\')
运行函数：aa.returndir()
'''
import os
class FindDir():
	def __init__(self,path):
		self.path=path
	def returndir(self):
		listdir=[]
		dirs=os.listdir(self.path)
		for i in dirs:
			if os.path.splitext(i)[1]=='.txt':  #分开文件名和扩展名
				listdir.append(i)
		return listdir
