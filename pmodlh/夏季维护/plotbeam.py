#用来处理波束测量数据 画成beam方向图

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib as mpl

myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=15) #标签字体
mpl.rcParams.update({'font.size': 10}) # 改变刻度所有字体大小，改变其他性质类似

x=np.linspace(1,96,96) #根据 数组大写改变
y=np.linspace(1,96,96)
x,y=np.meshgrid(x,y)

scan=np.loadtxt('0730_15mm_1m_03.dat')
scan[:,6]=10*(np.log10(scan[:,6]))-85.8; f0=scan[:,6] #功率瓦换算为dB
scan[:,7]=10*(np.log10(scan[:,7]))-85.8; f1=scan[:,7]
scan[:,8]=10*(np.log10(scan[:,8]))-85.8; f2=scan[:,8]
scan[:,9]=10*(np.log10(scan[:,9]))-85.8; f3=scan[:,9]
scan[:,10]=10*(np.log10(scan[:,10]))-85.8; f4=scan[:,10]
scan[:,11]=10*(np.log10(scan[:,11]))-85.8; f5=scan[:,11]
scan[:,12]=10*(np.log10(scan[:,12]))-85.8; f6=scan[:,12]
scan[:,13]=10*(np.log10(scan[:,13]))-85.8; f7=scan[:,13]
scan[:,14]=10*(np.log10(scan[:,14]))-85.8; f8=scan[:,14]

''' 查看数据质量
for i in scan[:,8]:
	print(i)
'''

n=int(np.sqrt(np.size(scan,0)))
f0=f0.reshape(n,n);f1=f1.reshape(n,n);f2=f2.reshape(n,n);f3=f3.reshape(n,n);f4=f4.reshape(n,n);f5=f5.reshape(n,n);f6=f6.reshape(n,n);f7=f7.reshape(n,n);f8=f8.reshape(n,n)
#for i in arange(0,n/2):
for i in range(0,int(n/2)):  #2020.07.31 python range函数不再支持步长 float型
	f0[2*i+1]=np.flipud(f0[2*i+1])
	f1[2*i+1]=np.flipud(f1[2*i+1])
	f2[2*i+1]=np.flipud(f2[2*i+1])
	f3[2*i+1]=np.flipud(f3[2*i+1])
	f4[2*i+1]=np.flipud(f4[2*i+1])
	f5[2*i+1]=np.flipud(f5[2*i+1])
	f6[2*i+1]=np.flipud(f6[2*i+1])
	f7[2*i+1]=np.flipud(f7[2*i+1])
	f8[2*i+1]=np.flipud(f8[2*i+1])

b1=np.hstack((f0,f1,f2)) #从(0,0)开始，beam1, beam2, beam3
b2=np.hstack((f3,f4,f5))              #b4, b5, ...
b3=np.hstack((f6,f7,f8))
b=np.vstack((b1,b2,b3))

fig=plt.figure(num=1, figsize=(10,8))
ax=plt.axes(projection='3d')
p=ax.plot_surface(x,y,b,cmap='jet'); fig.colorbar(p,shrink=0.5)
ax.set_xlabel('X',fontproperties=myfont)
ax.set_ylabel('Y',fontproperties=myfont)
ax.set_zlabel('dB',fontproperties=myfont)
ax.set_title('contour3D',fontproperties=myfont)
ax.view_init(60, 202.5)
ax.text(32, 32, -35, 'beam1', fontproperties=myfont, color='black'); ax.text(64, 32, -35, 'beam2'); ax.text(96, 32, -35, 'beam3') #x,y,z,s
ax.text(32, 64, -35, 'beam4'); ax.text(64, 64, -35, 'beam5'); ax.text(96, 64, -35, 'beam6')
ax.text(32, 96, -35, 'beam7'); ax.text(64, 96, -35, 'beam8'); ax.text(96, 96, -35, 'beam9')
plt.show()
