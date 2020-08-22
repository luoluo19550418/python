#读文件.py
#pandas读文件，返回时间和数据

import pandas as pd

def returndata2(path, filename): #
	dt,a20,a21=[],[],[]
	dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python')
	datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')  #date和time合成一列时间戳
	dt.extend(datetimes); a20.extend(dataset.values[:,20]); a21.extend(dataset.values[:,21])       # arr = np.zeros((len(years),7)); arr[:,0] = dataset.values[:,1]
	return dt,a20,a21

dt,a20,a21=returndata2('./2020.02/', 'record20200211.txt')

#读取多个文件（1个文件列表），追加到1个时间列表和1个数据列表
def returndata(path, listdir): #listdir is 所要读取的文件列表
	dt,a20,a21=[],[],[]
	for filename in listdir:
		dataset=pd.read_csv(path+filename,header=None,sep=' +',engine='python')
		datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')  #date和time合成一列时间戳
		dt.extend(datetimes); a20.extend(dataset.values[:,20]); a21.extend(dataset.values[:,21])
	return dt,a20,a21

dt,a20,a21=returndata('./2020.02/', listdir)
