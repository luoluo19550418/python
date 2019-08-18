#处理月面效率上下边带效率随年份的变化
import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('xiaolv.txt')
x=[2010,2011,2012,2013,2014,2015,2016,2017,2018]
xu,xl,eu,el=[],[],[],[]
for j in range(18):
	if (j%2)==0: #效率
		ux,lx=[],[]
		for i in range(18):
			if (i%2)==0: #上边带
				ux.append(data[i,j])
			else:
				lx.append(data[i,j])
		xu.append(ux)
		xl.append(lx)
	else: #std
		ue,le=[],[]
		for i in range(18):
			if (i%2)==0:
				ue.append(data[i,j])
			else:
				le.append(data[i,j])
		eu.append(ue)
		el.append(le)

xu=np.array(xu); xl=np.array(xl); eu=np.array(eu); el=np.array(el)
plt.figure(num=1,figsize=(20,10))
side=['USB','LSB']
beam=['beam1','beam2','beam3','beam4','beam5','beam6','beam7','beam8','beam9']
for i in range(9):
	plt.rcParams['xtick.direction'] = 'in'
	plt.rcParams['ytick.direction'] = 'in'
	plt.subplot(3,3,i+1)
	plt.errorbar(x,xu[0,:],eu[0,:],fmt='-o',capsize=3,capthick=1,label=side[0])
	plt.errorbar(x,xl[0,:],el[0,:],fmt='-o',capsize=3,capthick=1,label=side[1])
	plt.legend(loc='upper right')
	plt.xlabel('Year')
	plt.ylabel(r'$\eta$(%)') #插入希腊字母
	plt.text(2010,67,beam[i])
plt.show()

#由于2012年上边带没有数据，故沿用2011年上边带的数据。
