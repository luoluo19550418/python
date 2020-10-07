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
def readfile(path): # lots of files;  years using!
	dt,T,R,P = [],[],[],[]
	listdir = findfiles(path) #listdir is list of filename
	for filename in listdir: #merge same year
		strlist = ['2006', '2007', '2008', '2009','201001','201002','201003','201004','201005','201006','201007','201008','201009','201010','20101101','20101102','20101103','20101111','20101112'] #2006年-2010年 少了1列（只有一个边带的Tsys）20101113 数据中删了20101101-20101112
		try:
			print(filename[-12:-4]) #filename date
			if (filename[6:10] in strlist) or (filename[6:12] in strlist) or (filename[6:14] in strlist):
				dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); dataset = dataset.dropna(axis=0) #delete nan line
				datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
				dt.extend(datetimes); T.extend(dataset.values[:,12]); R.extend(dataset.values[:,13]); P.extend(dataset.values[:,14])
			else:
				dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python'); dataset = dataset.dropna(axis=0)
				datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')
				dt.extend(datetimes); T.extend(dataset.values[:,13]); R.extend(dataset.values[:,14]); P.extend(dataset.values[:,15])
		except: print('error opening ' + filename) #exception handing
	return dt,T,R,P
#dt,T,R,P = readfile(path+'2008/')

#f04，删除坏值
def delbad(arr): #异常值处理；nan ?
	Tmax = np.max(arr[:,1]); print('Tmax is starting!')
	while Tmax > 310: #max > 310, we delete the data in array; 37
		i = np.where(arr[:,1] == Tmax ); arr = np.delete(arr,i,axis=0) #删除第i行
		Tmax = np.max(arr[:,1]); print(Tmax)
	Tmin = np.min(arr[:,1]); print('Tmin is starting!')
	while Tmin < 238: #-35
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
#dt,T,R,P = readfile(path+'2008/') #记得路径 加 "/"
#arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
#arr = delbad(arr)

#f05，
def cycleyears(path):
	arr_all = np.empty((0,4),dtype=object);
	folders = findfolders(path)
	for folder in folders:
		dt,T,R,P = readfile(folder+'/')
		arr = np.empty((len(dt),4),dtype=object); arr[:,0]=dt; arr[:,1]=T; arr[:,2] = R; arr[:,3] = P
		arr = delbad(arr); #arr(year;T;R;P)
		arr_all = np.vstack((arr_all, arr));
	PWV=[]; print('Starting calculate PWV');
	for i in range(0,len(arr_all),1):
		Pvs = 6.105 * (273/float(arr_all[i,1]))**5.31 * np.exp(25.22*(float(arr_all[i,1])-273) / float(arr_all[i,1])); #饱和水气压(mbar)
		Pv = Pvs * arr_all[i,2]/100; #相对湿度百分比化成小数，Pv湿分压(mbar)
		rho = 2.17 * 10**(-4) * Pv / arr_all[i,1]; #水汽密度(g/cm-3)
		pwv = rho * 2000 * 1000; #大气垂直水柱高(mm)
		PWV.append(pwv);
	arr_all[:,1] = arr_all[:,1]-273.15;
	np.savetxt(path+'bPwv.dat', PWV, fmt="%.1f", delimiter='   ');
	np.savetxt(path+'bTep.dat', arr_all[:,1], fmt="%.1f", delimiter='   ');
	np.savetxt(path+'bHum.dat', arr_all[:,2], fmt="%.1f", delimiter='   ');
#cycleyears(path)

#f06，
def plohist(filec, num_bin, xlabel):
	dataset=pd.read_csv(path+filec,header=None,sep=' +',engine='python'); counts=[]; counts.extend(dataset.values[:,0]);
	fig=plt.figure(figsize=(15,10),dpi=80); ax1=fig.add_subplot(111); ax2=ax1.twinx()
	myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=30) #标签字体
	mpl.rcParams.update({'font.size': 20}) # 改变刻度所有字体大小，改变其他性质类似
	mpl.rcParams['xtick.direction'] = 'in'
	mpl.rcParams['ytick.direction'] = 'in'
	n, bins, patches = ax1.hist(counts, num_bin, rwidth=5, color='cyan', edgecolor='black', hatch='///', label="counts",); ax1.legend(loc='upper left')
#	ax1.set_xticks(bins,rotation=60)
	ax1.set_xlabel(xlabel); ax1.set_ylabel('counts');
	acc = [sum(n[:i])/len(counts) for i in range(len(n)+1)]
	ax2.plot(bins, acc, 'ro-', color='red', label="CDF"); ax2.legend(loc='upper right'); 
	ax2.set_ylabel('CDF(%)'); ax2.set_ylim(0,1.1); #ax2.set_xlim(xlim1,xlim2);
	ax2.grid(color='grey',linestyle='-.')
	plt.savefig(path+xlabel[0:3]+'.png')
#	plt.show()
#	return n,bins,patches
plohist('bPwv.dat', 22, 'PWV(mm)')
plohist('bTep.dat', 22, 'Teperature($^\circ$C)')
plohist('bHum.dat', 22, 'Humidity(%)')


'''
#f06，
def counts(path,file):
	print('Starting counts');
	dataset=pd.read_csv(path+file,header=None,sep=' +',engine='python');
	list=[]; list.extend(dataset.values[:,0]);
	counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #共22列
	if file=='bPwv.dat': index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] #21
	if file=='bTep.dat': index = [-30,-27,-24,-21,-18,-15,-12,-9,-6,-3,0,3,6,9,12,15,18,21,24,27,30] #21
	if file=='bHum.dat': index = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] #21
	for value in list:
		if value < index[0]: counts[0]=counts[0]+1;
		elif index[0] <= value < index[1]: counts[1]=counts[1]+1;
		elif index[1] <= value < index[2]: counts[2]=counts[2]+1;
		elif index[2] <= value < index[3]: counts[3]=counts[3]+1;
		elif index[3] <= value < index[4]: counts[4]=counts[4]+1;
		elif index[4] <= value < index[5]: counts[5]=counts[5]+1;
		elif index[5] <= value < index[6]: counts[6]=counts[6]+1;
		elif index[6] <= value < index[7]: counts[7]=counts[7]+1;
		elif index[7] <= value < index[8]: counts[8]=counts[8]+1;
		elif index[8] <= value < index[9]: counts[9]=counts[9]+1;
		elif index[9] <= value < index[10]: counts[10]=counts[10]+1;
		elif index[10] <= value < index[11]: counts[11]=counts[11]+1;
		elif index[11] <= value < index[12]: counts[12]=counts[12]+1;
		elif index[12] <= value < index[13]: counts[13]=counts[13]+1;
		elif index[13] <= value < index[14]: counts[14]=counts[14]+1;
		elif index[14] <= value < index[15]: counts[15]=counts[15]+1;
		elif index[15] <= value < index[16]: counts[16]=counts[16]+1;
		elif index[16] <= value < index[17]: counts[17]=counts[17]+1;
		elif index[17] <= value < index[18]: counts[18]=counts[18]+1;
		elif index[18] <= value < index[19]: counts[19]=counts[19]+1;
		elif index[19] <= value < index[20]: counts[20]=counts[20]+1;
		elif index[20] <= value: counts[21]=counts[21]+1;
	sum=0; pers = []; #归一化占比
	for count in counts: sum = sum+count;
	for count in counts: pers.append(round(100*count/sum,1));
	np.savetxt(path+'pers_'+file, pers, fmt="%.1f", delimiter='   ');
#counts(path,'bPwv.dat');
#counts(path,'bTep.dat');
#counts(path,'bHum.dat');
'''