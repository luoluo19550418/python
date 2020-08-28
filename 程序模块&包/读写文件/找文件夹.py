#filename: findfolder.py 遍历某路径下*02的文件夹
# -*- coding: utf-8 -*- 

def findfolders(path): # path 是路径
	list_dirs = os.walk(path); folders=[]
	for root,dirs,files in list_dirs:
		for d in dirs:
			if os.path.join(root,d)[-4:-2]=='20':  #os.path.join(root,d): path路径下的文件; #找20开头文件
				folders.append(os.path.join(root, d))
	return folders
folders = findfolders('../rawdata/')
