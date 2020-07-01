#for循环找文件
#purpose：找某路径下的"*.txt"文件

import os

def returndir(path):
	listdir=[]
	dirs=os.listdir(path)
	for i in dirs:
		if os.path.splitext(i)[1]=='.txt':  #分开文件名和扩展名
			listdir.append(i)
	return listdir

listdir=returndir('2020.02')
