#script: ployears.py

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
		print(filename[-12:-4]) #filename date
		if (filename[6:10] in strlist) or (filename[6:12] in strlist) or (filename[6:14] in strlist):
			dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); dataset = dataset.dropna(axis=0)
			datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
			dt.extend(datetimes); T.extend(dataset.values[:,12]); R.extend(dataset.values[:,13]); P.extend(dataset.values[:,14])
		else:
			dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); dataset = dataset.dropna(axis=0)
			datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
			dt.extend(datetimes); T.extend(dataset.values[:,13]); R.extend(dataset.values[:,14]); P.extend(dataset.values[:,15])
	except: print('error opening ' + filename)
	return dt,T,R,P
#dt,T,R,P = readfile(path+'2006/', 'record20060101.txt')

#f04，删除坏值
def delbad(arr): #异常值处理；nan ?
	try:
		Tmax = np.max(arr[:,1]); print('Tmax is starting!')
		while Tmax > 310: #max > 330, we delete the data in array
			i = np.where(arr[:,1] == Tmax ); arr = np.delete(arr,i,axis=0) #删除第i行
			Tmax = np.max(arr[:,1]); print(Tmax)
		Tmin = np.min(arr[:,1]); print('Tmin is starting!')
		while Tmin < 238:
			i = np.where( arr[:,1] == Tmin ); arr = np.delete(arr,i,axis=0)
			Tmin = np.min(arr[:,1]); print(Tmin)
		Rmax = np.max(arr[:,2]); print('Rmax is starting!')
		while Rmax > 100:
			i = np.where( arr[:,2] == Rmax ); arr = np.delete(arr,i,axis=0)
			Rmax = np.max(arr[:,2]); print(Rmax)
		Rmin = np.min(arr[:,2]); print('Rmin is starting!')
		while Rmin < 2.5:
			i = np.where( arr[:,2] == Rmin ); arr = np.delete(arr,i,axis=0)
			Rmin = np.min(arr[:,2]); print(Rmin)
		Pmax = np.max(arr[:,3]); print('Pmax is starting!')
		while Pmax > 704:
			i = np.where( arr[:,3] == Pmax ); arr = np.delete(arr,i,axis=0)
			Pmax = np.max(arr[:,3]); print(Pmax)
		Pmin = np.min(arr[:,3]); print('Pmin is starting!')
		while Pmin < 660:
			i = np.where( arr[:,3] == Pmin ); arr = np.delete(arr,i,axis=0)
			Pmin = np.min(arr[:,3]); print(Pmin)
		return arr
	except: return np.empty((0,4),dtype=object) #空数组

#f05，数据按月分开
def prodata(path):
	folders = findfolders(path)
	arrtmp = np.empty((0,4),dtype=object);
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
					if filename[10:12] == '01': arr1=np.vstack((arr1,arr_var))
					if filename[10:12] == '02': arr2=np.vstack((arr2,arr_var))
					if filename[10:12] == '03': arr3=np.vstack((arr3,arr_var))
					if filename[10:12] == '04': arr4=np.vstack((arr4,arr_var))
					if filename[10:12] == '05': arr5=np.vstack((arr5,arr_var))
					if filename[10:12] == '06': arr6=np.vstack((arr6,arr_var))
					if filename[10:12] == '07': arr7=np.vstack((arr7,arr_var))
					if filename[10:12] == '08': arr8=np.vstack((arr8,arr_var))
					if filename[10:12] == '09': arr9=np.vstack((arr9,arr_var))
					if filename[10:12] == '10': arr10=np.vstack((arr10,arr_var))
					if filename[10:12] == '11': arr11=np.vstack((arr11,arr_var))
					if filename[10:12] == '12': arr12=np.vstack((arr12,arr_var))
	arr = [arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12]
	arr_days = np.empty((0,10),dtype=object)
	for i in range(0,12,1):
		arr_day = np.array([i+1,np.max(arr[i][:,1]),np.median(arr[i][:,1]),np.min(arr[i][:,1]), np.max(arr[i][:,2]),np.median(arr[i][:,2]),np.min(arr[i][:,2]), np.max(arr[i][:,3]),np.median(arr[i][:,3]),np.min(arr[i][:,3])])
		arr_days = np.vstack((arr_days, arr_day))
	np.savetxt(path+'arr_days.dat', arr_days, fmt="%.1f", delimiter='   ')
#prodata(path)

def plomonths(path,file):
	years=[]; dataset=pd.read_csv(path+file,header=None,sep=' +',engine='python')
	years.extend(dataset.values[:,0]); arr_years = np.zeros((len(years),10)) #单独以 years 为 list 是因为定义 arr 要用到
	arr_years[:,0]=dataset.values[:,0]
	arr_years[:,1]=dataset.values[:,1]; arr_years[:,2]=dataset.values[:,2]; arr_years[:,3]=dataset.values[:,3]
	arr_years[:,4]=dataset.values[:,4]; arr_years[:,5]=dataset.values[:,5]; arr_years[:,6]=dataset.values[:,6]
	arr_years[:,7]=dataset.values[:,7]; arr_years[:,8]=dataset.values[:,8]; arr_years[:,9]=dataset.values[:,9]
	print(np.max(arr_years[:,1]), np.median(arr_years[:,2]), np.min(arr_years[:,3]));
	print(np.max(arr_years[:,4]), np.median(arr_years[:,5]), np.min(arr_years[:,6]));
	print(np.max(arr_years[:,7]), np.median(arr_years[:,8]), np.min(arr_years[:,9]));
	plt.figure(figsize=(20,10))
	label=['months','Tmax','Tmedian','Tmin','Rmax','Rmedian','Rmin','Pmax','Pmedian','Pmin']
	myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=20) #标签字体
	mpl.rcParams.update({'font.size': 10}) # 改变刻度所有字体大小，改变其他性质类似
	for col in range(1,len(arr_years[0,:]),1):
		if col < 4:
			plt.subplot(131)
			plt.plot(arr_years[:,0],arr_years[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_years[:,0],rotation=60); plt.grid(color='cyan', linestyle='--') #蓝绿色
			plt.title('Temperature variation', fontproperties=myfont)
		elif col < 7:
			plt.subplot(132)
			plt.plot(arr_years[:,0],arr_years[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_years[:,0],rotation=60);plt.grid(color='cyan', linestyle='--')
			plt.title('Humidity variation', fontproperties=myfont)
		elif col < 11:
			plt.subplot(133)
			plt.plot(arr_years[:,0],arr_years[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_years[:,0],rotation=60); plt.grid(color='cyan', linestyle='--')
			plt.title('pressure variation', fontproperties=myfont)
	plt.savefig(path+'arr_days.png')
prodata(path)
plomonths(path,'arr_days.dat')
