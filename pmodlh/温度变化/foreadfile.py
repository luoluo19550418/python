#for循环读文件
import pandas as pd
class ForeadFile():
	def __init__(self,path,listdir):
		self.listdir=listdir; self.path=path
	def returndata(self):
		dt,a20,a21=[],[],[]
		for filename in self.listdir:
			dataset=pd.read_csv(self.path+filename,header=None,sep=' +',engine='python')
			datetimes=pd.to_datetime(dataset.values[:,0]) + pd.to_timedelta(dataset.values[:,1],unit='h')  #date和time合成一列时间戳
			dt.extend(datetimes); a20.extend(dataset.values[:,20]); a21.extend(dataset.values[:,21])
		return dt,a20,a21
