#script: plomonths.py

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
			dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); dataset = dataset.dropna(axis=0); #x,y=dataset.shape
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
		Tmax = np.max(arr[:,1]);
		while Tmax > 310: #max > 330, we delete the data in array
			i = np.where(arr[:,1] == Tmax ); arr = np.delete(arr,i,axis=0) #删除第i行
			Tmax = np.max(arr[:,1]); print(Tmax)
		Tmin = np.min(arr[:,1]);
		while Tmin < 238:
			i = np.where( arr[:,1] == Tmin ); arr = np.delete(arr,i,axis=0)
			Tmin = np.min(arr[:,1]); print(Tmin)
		Rmax = np.max(arr[:,2]);
		while Rmax > 100:
			i = np.where( arr[:,2] == Rmax ); arr = np.delete(arr,i,axis=0)
			Rmax = np.max(arr[:,2]); print(Rmax)
		Rmin = np.min(arr[:,2]);
		while Rmin < 2.5:
			i = np.where( arr[:,2] == Rmin ); arr = np.delete(arr,i,axis=0)
			Rmin = np.min(arr[:,2]); print(Rmin)
		Pmax = np.max(arr[:,3]);
		while Pmax > 704:
			i = np.where( arr[:,3] == Pmax ); arr = np.delete(arr,i,axis=0)
			Pmax = np.max(arr[:,3]); print(Pmax)
		Pmin = np.min(arr[:,3]);
		while Pmin < 660:
			i = np.where( arr[:,3] == Pmin ); arr = np.delete(arr,i,axis=0)
			Pmin = np.min(arr[:,3]); print(Pmin)
		return arr
	except: return np.empty((0,4),dtype=object) #空数组

#f05，数据按时平均
def prodata(path):
	folders = findfolders(path)
	arrtmp=np.empty((0,4),dtype=object);
	arr0,arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12,arr13,arr14,arr15,arr16,arr17,arr18,arr19,arr20,arr21,arr22,arr23 = arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp,arrtmp
	for folder in folders:
		listdir = findfiles(folder+'/')
		for filename in listdir:
			dt,T,R,P = readfile(folder+'/',filename); arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
			arr = delbad(arr); #arr(time;T;R;P)
			arr_var = np.empty((1,4),dtype=object); #1 row 4 columns; 也可用 list
			if len(arr) > 0:
				arr_var[0,0] = filename[-12:-4]; arr_var[0,1] = np.max(arr[:,1])-np.min(arr[:,1]); arr_var[0,2] = np.max(arr[:,2])-np.min(arr[:,2]); arr_var[0,3] = np.max(arr[:,3])-np.min(arr[:,3]) #周日变化
				if arr_var[0,1]>1 and arr_var[0,2]>5 and arr_var[0,3]>0.5: #坏值阈值
					for i in range(0,len(arr),1):
						if str(arr[i][0])[11:13] == '00': arr0=np.vstack((arr0,arr[i]))
						if str(arr[i][0])[11:13] == '01': arr1=np.vstack((arr1,arr[i]))
						if str(arr[i][0])[11:13] == '02': arr2=np.vstack((arr2,arr[i]))
						if str(arr[i][0])[11:13] == '03': arr3=np.vstack((arr3,arr[i]))
						if str(arr[i][0])[11:13] == '04': arr4=np.vstack((arr4,arr[i]))
						if str(arr[i][0])[11:13] == '05': arr5=np.vstack((arr5,arr[i]))
						if str(arr[i][0])[11:13] == '06': arr6=np.vstack((arr6,arr[i]))
						if str(arr[i][0])[11:13] == '07': arr7=np.vstack((arr7,arr[i]))
						if str(arr[i][0])[11:13] == '08': arr8=np.vstack((arr8,arr[i]))
						if str(arr[i][0])[11:13] == '09': arr9=np.vstack((arr9,arr[i]))
						if str(arr[i][0])[11:13] == '10': arr10=np.vstack((arr10,arr[i]))
						if str(arr[i][0])[11:13] == '11': arr11=np.vstack((arr11,arr[i]))
						if str(arr[i][0])[11:13] == '12': arr12=np.vstack((arr12,arr[i]))
						if str(arr[i][0])[11:13] == '13': arr13=np.vstack((arr13,arr[i]))
						if str(arr[i][0])[11:13] == '14': arr14=np.vstack((arr14,arr[i]))
						if str(arr[i][0])[11:13] == '15': arr15=np.vstack((arr15,arr[i]))
						if str(arr[i][0])[11:13] == '16': arr16=np.vstack((arr16,arr[i]))
						if str(arr[i][0])[11:13] == '17': arr17=np.vstack((arr17,arr[i]))
						if str(arr[i][0])[11:13] == '18': arr18=np.vstack((arr18,arr[i]))
						if str(arr[i][0])[11:13] == '19': arr19=np.vstack((arr19,arr[i]))
						if str(arr[i][0])[11:13] == '20': arr20=np.vstack((arr20,arr[i]))
						if str(arr[i][0])[11:13] == '21': arr21=np.vstack((arr21,arr[i]))
						if str(arr[i][0])[11:13] == '22': arr22=np.vstack((arr22,arr[i]))
						if str(arr[i][0])[11:13] == '23': arr23=np.vstack((arr23,arr[i]))
	arr=np.empty((24,10),dtype=object);
	arr[0,0]=0; arr[0,1]=np.max(arr0[:,1]);arr[0,2]=np.median(arr0[:,1]);arr[0,3]=np.min(arr0[:,1]); arr[0,4]=np.max(arr0[:,2]); arr[0,5]=np.median(arr0[:,2]); arr[0,6]=np.min(arr0[:,2]); arr[0,7]=np.max(arr0[:,3]); arr[0,8]=np.median(arr0[:,3]); arr[0,9]=np.min(arr0[:,3])
	arr[1,0]=1; arr[1,1]=np.max(arr1[:,1]);arr[1,2]=np.median(arr1[:,1]);arr[1,3]=np.min(arr1[:,1]); arr[1,4]=np.max(arr1[:,2]); arr[1,5]=np.median(arr1[:,2]); arr[1,6]=np.min(arr1[:,2]); arr[1,7]=np.max(arr1[:,3]); arr[1,8]=np.median(arr1[:,3]); arr[1,9]=np.min(arr1[:,3])
	arr[2,0]=2; arr[2,1]=np.max(arr2[:,1]);arr[2,2]=np.median(arr2[:,1]);arr[2,3]=np.min(arr2[:,1]); arr[2,4]=np.max(arr2[:,2]); arr[2,5]=np.median(arr2[:,2]); arr[2,6]=np.min(arr2[:,2]); arr[2,7]=np.max(arr2[:,3]); arr[2,8]=np.median(arr2[:,3]); arr[2,9]=np.min(arr2[:,3])
	arr[3,0]=3; arr[3,1]=np.max(arr3[:,1]);arr[3,2]=np.median(arr3[:,1]);arr[3,3]=np.min(arr3[:,1]); arr[3,4]=np.max(arr3[:,2]); arr[3,5]=np.median(arr3[:,2]); arr[3,6]=np.min(arr3[:,2]); arr[3,7]=np.max(arr3[:,3]); arr[3,8]=np.median(arr3[:,3]); arr[3,9]=np.min(arr3[:,3])
	arr[4,0]=4; arr[4,1]=np.max(arr4[:,1]);arr[4,2]=np.median(arr4[:,1]);arr[4,3]=np.min(arr4[:,1]); arr[4,4]=np.max(arr4[:,2]); arr[4,5]=np.median(arr4[:,2]); arr[4,6]=np.min(arr4[:,2]); arr[4,7]=np.max(arr4[:,3]); arr[4,8]=np.median(arr4[:,3]); arr[4,9]=np.min(arr4[:,3])
	arr[5,0]=5; arr[5,1]=np.max(arr5[:,1]);arr[5,2]=np.median(arr5[:,1]);arr[5,3]=np.min(arr5[:,1]); arr[5,4]=np.max(arr5[:,2]); arr[5,5]=np.median(arr5[:,2]); arr[5,6]=np.min(arr5[:,2]); arr[5,7]=np.max(arr5[:,3]); arr[5,8]=np.median(arr5[:,3]); arr[5,9]=np.min(arr5[:,3])
	arr[6,0]=6; arr[6,1]=np.max(arr6[:,1]);arr[6,2]=np.median(arr6[:,1]);arr[6,3]=np.min(arr6[:,1]); arr[6,4]=np.max(arr6[:,2]); arr[6,5]=np.median(arr6[:,2]); arr[6,6]=np.min(arr6[:,2]); arr[6,7]=np.max(arr6[:,3]); arr[6,8]=np.median(arr6[:,3]); arr[6,9]=np.min(arr6[:,3])
	arr[7,0]=7; arr[7,1]=np.max(arr7[:,1]);arr[7,2]=np.median(arr7[:,1]);arr[7,3]=np.min(arr7[:,1]); arr[7,4]=np.max(arr7[:,2]); arr[7,5]=np.median(arr7[:,2]); arr[7,6]=np.min(arr7[:,2]); arr[7,7]=np.max(arr7[:,3]); arr[7,8]=np.median(arr7[:,3]); arr[7,9]=np.min(arr7[:,3])
	arr[8,0]=8; arr[8,1]=np.max(arr8[:,1]);arr[8,2]=np.median(arr8[:,1]);arr[8,3]=np.min(arr8[:,1]); arr[8,4]=np.max(arr8[:,2]); arr[8,5]=np.median(arr8[:,2]); arr[8,6]=np.min(arr8[:,2]); arr[8,7]=np.max(arr8[:,3]); arr[8,8]=np.median(arr8[:,3]); arr[8,9]=np.min(arr8[:,3])
	arr[9,0]=9; arr[9,1]=np.max(arr9[:,1]);arr[9,2]=np.median(arr9[:,1]);arr[9,3]=np.min(arr9[:,1]); arr[9,4]=np.max(arr9[:,2]); arr[9,5]=np.median(arr9[:,2]); arr[9,6]=np.min(arr9[:,2]); arr[9,7]=np.max(arr9[:,3]); arr[9,8]=np.median(arr9[:,3]); arr[9,9]=np.min(arr9[:,3])
	arr[10,0]=10; arr[10,1]=np.max(arr10[:,1]);arr[10,2]=np.median(arr10[:,1]);arr[10,3]=np.min(arr10[:,1]); arr[10,4]=np.max(arr10[:,2]); arr[10,5]=np.median(arr10[:,2]); arr[10,6]=np.min(arr10[:,2]); arr[10,7]=np.max(arr10[:,3]); arr[10,8]=np.median(arr10[:,3]); arr[10,9]=np.min(arr10[:,3])
	arr[11,0]=11; arr[11,1]=np.max(arr11[:,1]);arr[11,2]=np.median(arr11[:,1]);arr[11,3]=np.min(arr11[:,1]); arr[11,4]=np.max(arr11[:,2]); arr[11,5]=np.median(arr11[:,2]); arr[11,6]=np.min(arr11[:,2]); arr[11,7]=np.max(arr11[:,3]); arr[11,8]=np.median(arr11[:,3]); arr[11,9]=np.min(arr11[:,3])
	arr[12,0]=12; arr[12,1]=np.max(arr12[:,1]);arr[12,2]=np.median(arr12[:,1]);arr[12,3]=np.min(arr12[:,1]); arr[12,4]=np.max(arr12[:,2]); arr[12,5]=np.median(arr12[:,2]); arr[12,6]=np.min(arr12[:,2]); arr[12,7]=np.max(arr12[:,3]); arr[12,8]=np.median(arr12[:,3]); arr[12,9]=np.min(arr12[:,3])
	arr[13,0]=13; arr[13,1]=np.max(arr13[:,1]);arr[13,2]=np.median(arr13[:,1]);arr[13,3]=np.min(arr13[:,1]); arr[13,4]=np.max(arr13[:,2]); arr[13,5]=np.median(arr13[:,2]); arr[13,6]=np.min(arr13[:,2]); arr[13,7]=np.max(arr13[:,3]); arr[13,8]=np.median(arr13[:,3]); arr[13,9]=np.min(arr13[:,3])
	arr[14,0]=14; arr[14,1]=np.max(arr14[:,1]);arr[14,2]=np.median(arr14[:,1]);arr[14,3]=np.min(arr14[:,1]); arr[14,4]=np.max(arr14[:,2]); arr[14,5]=np.median(arr14[:,2]); arr[14,6]=np.min(arr14[:,2]); arr[14,7]=np.max(arr14[:,3]); arr[14,8]=np.median(arr14[:,3]); arr[14,9]=np.min(arr14[:,3])
	arr[15,0]=15; arr[15,1]=np.max(arr15[:,1]);arr[15,2]=np.median(arr15[:,1]);arr[15,3]=np.min(arr15[:,1]); arr[15,4]=np.max(arr15[:,2]); arr[15,5]=np.median(arr15[:,2]); arr[15,6]=np.min(arr15[:,2]); arr[15,7]=np.max(arr15[:,3]); arr[15,8]=np.median(arr15[:,3]); arr[15,9]=np.min(arr15[:,3])
	arr[16,0]=16; arr[16,1]=np.max(arr16[:,1]);arr[16,2]=np.median(arr16[:,1]);arr[16,3]=np.min(arr16[:,1]); arr[16,4]=np.max(arr16[:,2]); arr[16,5]=np.median(arr16[:,2]); arr[16,6]=np.min(arr16[:,2]); arr[16,7]=np.max(arr16[:,3]); arr[16,8]=np.median(arr16[:,3]); arr[16,9]=np.min(arr16[:,3])
	arr[17,0]=17; arr[17,1]=np.max(arr17[:,1]);arr[17,2]=np.median(arr17[:,1]);arr[17,3]=np.min(arr17[:,1]); arr[17,4]=np.max(arr17[:,2]); arr[17,5]=np.median(arr17[:,2]); arr[17,6]=np.min(arr17[:,2]); arr[17,7]=np.max(arr17[:,3]); arr[17,8]=np.median(arr17[:,3]); arr[17,9]=np.min(arr17[:,3])
	arr[18,0]=18; arr[18,1]=np.max(arr18[:,1]);arr[18,2]=np.median(arr18[:,1]);arr[18,3]=np.min(arr18[:,1]); arr[18,4]=np.max(arr18[:,2]); arr[18,5]=np.median(arr18[:,2]); arr[18,6]=np.min(arr18[:,2]); arr[18,7]=np.max(arr18[:,3]); arr[18,8]=np.median(arr18[:,3]); arr[18,9]=np.min(arr18[:,3])
	arr[19,0]=19; arr[19,1]=np.max(arr19[:,1]);arr[19,2]=np.median(arr19[:,1]);arr[19,3]=np.min(arr19[:,1]); arr[19,4]=np.max(arr19[:,2]); arr[19,5]=np.median(arr19[:,2]); arr[19,6]=np.min(arr19[:,2]); arr[19,7]=np.max(arr19[:,3]); arr[19,8]=np.median(arr19[:,3]); arr[19,9]=np.min(arr19[:,3])
	arr[20,0]=20; arr[20,1]=np.max(arr20[:,1]);arr[20,2]=np.median(arr20[:,1]);arr[20,3]=np.min(arr20[:,1]); arr[20,4]=np.max(arr20[:,2]); arr[20,5]=np.median(arr20[:,2]); arr[20,6]=np.min(arr20[:,2]); arr[20,7]=np.max(arr20[:,3]); arr[20,8]=np.median(arr20[:,3]); arr[20,9]=np.min(arr20[:,3])
	arr[21,0]=21; arr[21,1]=np.max(arr21[:,1]);arr[21,2]=np.median(arr21[:,1]);arr[21,3]=np.min(arr21[:,1]); arr[21,4]=np.max(arr21[:,2]); arr[21,5]=np.median(arr21[:,2]); arr[21,6]=np.min(arr21[:,2]); arr[21,7]=np.max(arr21[:,3]); arr[21,8]=np.median(arr21[:,3]); arr[21,9]=np.min(arr21[:,3])
	arr[22,0]=22; arr[22,1]=np.max(arr22[:,1]);arr[22,2]=np.median(arr22[:,1]);arr[22,3]=np.min(arr22[:,1]); arr[22,4]=np.max(arr22[:,2]); arr[22,5]=np.median(arr22[:,2]); arr[22,6]=np.min(arr22[:,2]); arr[22,7]=np.max(arr22[:,3]); arr[22,8]=np.median(arr22[:,3]); arr[22,9]=np.min(arr22[:,3])
	arr[23,0]=23; arr[23,1]=np.max(arr23[:,1]);arr[23,2]=np.median(arr23[:,1]);arr[23,3]=np.min(arr23[:,1]); arr[23,4]=np.max(arr23[:,2]); arr[23,5]=np.median(arr23[:,2]); arr[23,6]=np.min(arr23[:,2]); arr[23,7]=np.max(arr23[:,3]); arr[23,8]=np.median(arr23[:,3]); arr[23,9]=np.min(arr23[:,3])
	np.savetxt(path+'arr_hours.dat', arr, fmt="%.1f", delimiter='   ')
#prodata(path)

def plohours(path):
	months=[]; dataset=pd.read_csv('../rawdata/arr_hours.dat',header=None,sep=' +',engine='python')
	months.extend(dataset.values[:,0]); arr_hours = np.zeros((len(months),10)) #单独以 months 为 list 是因为定义 arr 要用到
	arr_hours[:,0]=dataset.values[:,0]
	arr_hours[:,1]=dataset.values[:,1]; arr_hours[:,2]=dataset.values[:,2]; arr_hours[:,3]=dataset.values[:,3]
	arr_hours[:,4]=dataset.values[:,4]; arr_hours[:,5]=dataset.values[:,5]; arr_hours[:,6]=dataset.values[:,6]
	arr_hours[:,7]=dataset.values[:,7]; arr_hours[:,8]=dataset.values[:,8]; arr_hours[:,9]=dataset.values[:,9]
	arr_hours[:,1]=arr_hours[:,1]-273.15; arr_hours[:,2]=arr_hours[:,2]-273.15; arr_hours[:,3]=arr_hours[:,3]-273.15
#	print(np.max(arr_hours[:,1]), np.median(arr_hours[:,2]), np.min(arr_hours[:,3]));
#	print(np.max(arr_hours[:,4]), np.median(arr_hours[:,5]), np.min(arr_hours[:,6]));
#	print(np.max(arr_hours[:,7]), np.median(arr_hours[:,8]), np.min(arr_hours[:,9]));
	plt.figure(figsize=(20,10))
	label=['months','Tmax','Tmedian','Tmin','Rmax','Rmedian','Rmin','Pmax','Pmedian','Pmin']
	myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=20) #标签字体
	mpl.rcParams.update({'font.size': 10}) # 改变刻度所有字体大小，改变其他性质类似
	for col in range(1,len(arr_hours[0,:]),1):
		if col < 4:
			plt.subplot(131)
			plt.plot(arr_hours[:,0],arr_hours[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_hours[:,0],rotation=60); plt.grid(color='cyan', linestyle='--') #蓝绿色
			plt.title('Temperature variation', fontproperties=myfont)
		elif col < 7:
			plt.subplot(132)
			plt.plot(arr_hours[:,0],arr_hours[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_hours[:,0],rotation=60);plt.grid(color='cyan', linestyle='--')
			plt.title('Humidity variation', fontproperties=myfont)
		elif col < 11:
			plt.subplot(133)
			plt.plot(arr_hours[:,0],arr_hours[:,col],linestyle='-', marker='o',label=label[col]); plt.legend(loc='upper right')
			plt.xticks(arr_hours[:,0],rotation=60); plt.grid(color='cyan', linestyle='--')
			plt.title('pressure variation', fontproperties=myfont)
	plt.savefig(path+'arr_hours.png')
#plohours(path)

months=[]; dataset=pd.read_csv('../rawdata/arr_hours.dat',header=None,sep=' +',engine='python')
months.extend(dataset.values[:,0]); arr_hours = np.zeros((len(months),10)) #单独以 months 为 list 是因为定义 arr 要用到
arr_hours[:,0]=dataset.values[:,0]
arr_hours[:,1]=dataset.values[:,1]; arr_hours[:,2]=dataset.values[:,2]; arr_hours[:,3]=dataset.values[:,3]
arr_hours[:,4]=dataset.values[:,4]; arr_hours[:,5]=dataset.values[:,5]; arr_hours[:,6]=dataset.values[:,6]
arr_hours[:,7]=dataset.values[:,7]; arr_hours[:,8]=dataset.values[:,8]; arr_hours[:,9]=dataset.values[:,9]
arr_hours[:,1]=arr_hours[:,1]-273.15; arr_hours[:,2]=arr_hours[:,2]-273.15; arr_hours[:,3]=arr_hours[:,3]-273.15
plt.plot(arr_hours[:,2],arr_hours[:,5],'.')#,label=label[col]); plt.legend(loc='upper right')
plt.show()