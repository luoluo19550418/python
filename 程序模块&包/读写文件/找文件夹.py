#filename: findfolder.py 遍历某路径下*02的文件夹
# -*- coding: utf-8 -*- 

import os 

def returnfolder(rootdir): # rootdir is path（路径）
	list_dirs = os.walk(rootdir); folder=[]
	for root,dirs,files in list_dirs:
		for d in dirs:
			if os.path.join(root,d)[-2:]=='02':  #os.path.join(root,d): rootdir路径下的文件
				folder.append(os.path.join(root, d))
	return folder

folder=returnfolder('./')
