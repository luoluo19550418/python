#script: findbad.py
#aim: 找异常数据

import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

path='../rawdata/'
#f01，在某路径下查找符合条件的文件夹，返回list
def findfolders(path):
	list_dirs = os.walk(path); folders=[]
	for root,dirs,files in list_dirs:
		for d in dirs:
			if os.path.join(root,d)[-4:-2]=='20':  #os.path.join(root,d): path路径下的文件; #找20开头文件
				folders.append(os.path.join(root, d))
	return folders
#folders = findfolders(path)  #"../rawdata/2006"

#f02，在某目录下查找符合条件的文件，返回list
def findfiles(path):
	listdir=[]
	dirs=os.listdir(path)
	for i in dirs:
		if os.path.splitext(i)[1]=='.txt':  #分开文件名和扩展名
			listdir.append(i)
	return listdir
#listdir = findfiles(path)

#f03，读文件
def readfile(path, filename): #single file; months using!
	dt,T,R,P = [],[],[],[]
	strlist = ['2006', '2007', '2008', '2009','201001','201002','201003','201004','201005','201006','201007','201008','201009','201010','20101101','20101102','20101103','20101111','20101112']
	try:
		if (filename[6:10] in strlist) or (filename[6:12] in strlist) or (filename[6:14] in strlist):
			dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); #x,y=dataset.shape
			datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
			dt.extend(datetimes); T.extend(dataset.values[:,12]); R.extend(dataset.values[:,13]); P.extend(dataset.values[:,14])
		else:
			dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python')
			datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
			dt.extend(datetimes); T.extend(dataset.values[:,13]); R.extend(dataset.values[:,14]); P.extend(dataset.values[:,15])
	except: print('error opening ' + filename)
	return dt,T,R,P
#dt,T,R,P = readfile(path+'2006/', 'record20060101.txt')

#f04，删除坏值
def delbad(arr): #异常值根据实际情况修改
	try:
		Tmax = np.max(arr[:,1]);
		while Tmax > 330: #max > 330, we delete the data in array
			i = np.where(arr[:,1] == Tmax ); arr = np.delete(arr,i,axis=0) #删除第i行
			Tmax = np.max(arr[:,1]);
		Tmin = np.min(arr[:,1]);
		while Tmin < 200:
			i = np.where( arr[:,1] == Tmin ); arr = np.delete(arr,i,axis=0)
			Tmin = np.min(arr[:,1]);
		Rmax = np.max(arr[:,2]);
		while Rmax > 100:
			i = np.where( arr[:,2] == Rmax ); arr = np.delete(arr,i,axis=0)
			Rmax = np.max(arr[:,2]);
		Rmin = np.min(arr[:,2]);
		while Rmin < 0:
			i = np.where( arr[:,2] == Rmin ); arr = np.delete(arr,i,axis=0)
			Rmin = np.min(arr[:,2]);
		Pmax = np.max(arr[:,3]);
		while Pmax > 800:
			i = np.where( arr[:,3] == Pmax ); arr = np.delete(arr,i,axis=0)
			Pmax = np.max(arr[:,3]);
		Pmin = np.min(arr[:,3]);
		while Pmin < 600:
			i = np.where( arr[:,3] == Pmin ); arr = np.delete(arr,i,axis=0)
			Pmin = np.min(arr[:,3]);
		return arr
	except: return np.empty((0,4),dtype=object) #空数组

def findbad1(path,bad): #找极大极小异常值 所在文件
	folders = findfolders(path)
	arrtmp = np.empty((0,4),dtype=object);
	arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12=arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp
	for folder in folders:
		listdir = findfiles(folder+'/')
		for filename in listdir:
			dt,T,R,P = readfile(folder+'/',filename); arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
			arr = delbad(arr); #arr(year;T;R;P)
			if filename[10:12]=='08':
				if bad in arr:
					print(filename)
#findbad1(path,270.0) #找异常值 0 等

def findbad2(path): #找包含恒定数值的文件
	folders = findfolders(path)
	arrtmp = np.empty((0,4),dtype=object);
	arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12 = arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp
	for folder in folders:
		listdir = findfiles(folder+'/')
		for filename in listdir:
			dt,T,R,P = readfile(folder+'/',filename); arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
			arr = delbad(arr); #arr(year;T;R;P)
			arr_var = np.empty((1,4),dtype=object); #1 row 4 columns; 也可用 list
			if len(arr) > 0:
				arr_var[0,0] = filename[-12:-4]; arr_var[0,1] = np.max(arr[:,1])-np.min(arr[:,1]); arr_var[0,2] = np.max(arr[:,2])-np.min(arr[:,2]); arr_var[0,3] = np.max(arr[:,3])-np.min(arr[:,3]) #周日变化
				#if arr_var[0,1]<=1 or arr_var[0,2]<=5 or arr_var[0,3]<=0.5: #修改 arr_var[0,1] arr_var[0,2] arr_var[0,3] 的阈值
				if arr_var[0,3] > 16:
					print(filename)
#findbad2(path)

def find0102(path): #找1，2月数据
	folders = findfolders(path)
	arrtmp=np.empty((0,4),dtype=object);
	arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12=arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp
	for folder in folders:
		listdir = findfiles(folder+'/')
		for filename in listdir:
			dt,T,R,P = readfile(folder+'/',filename); arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
			arr = delbad(arr); #arr(year;T;R;P)
			arr_var = np.empty((1,4),dtype=object); #1 row 4 columns; 也可用 list
			if len(arr) > 0:
				arr_var[0,0] = filename[-12:-4]; arr_var[0,1] = np.max(arr[:,1])-np.min(arr[:,1]); arr_var[0,2] = np.max(arr[:,2])-np.min(arr[:,2]); arr_var[0,3] = np.max(arr[:,3])-np.min(arr[:,3]) #周日变化
				if arr_var[0,1]>1 and arr_var[0,2]>5 and arr_var[0,3]>0.5: #坏值阈值
					if filename[10:12] == '01': arr1=np.vstack((arr1,arr))
					if filename[10:12] == '02': arr2=np.vstack((arr2,arr))
	np.savetxt(path+'month01.dat', arr1, fmt="%s", delimiter='   ')
	np.savetxt(path+'month02.dat', arr2, fmt="%s", delimiter='   ')
	R=[]; dataset=pd.read_csv('../rawdata/month02.dat',header=None,sep=' +',engine='python') #'../rawdata/month02.dat'文件可修改
	R.extend(dataset.values[:,3]);
	plt.plot(R)
	plt.show()
#find0102(path)


