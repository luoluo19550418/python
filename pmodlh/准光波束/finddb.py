import os,sys
import glob
import numpy as np
import math
import matplotlib.pyplot as plt

d,l0,l1,l2=1.075,5.561,1,2
r0=d/2
r1=(r0*l1/l0)*1000;r2=(r0*l2/l0)*1000
arc=math.atan(r0/l0);deg=180*arc/math.pi
print r1,r2,deg

#filename='2019-2m/2D_15mm_2m_08.dat'
filename='2019-1m/1m2D15mm-004.dat'
scan=np.loadtxt(filename)
scan[:,10]=10*(np.log10(scan[:,10]))-85.8; f5=(scan[:,10]) #功率瓦换算为dB

n=int(np.sqrt(np.size(scan,0)))
s=scan[:,1].reshape(n,n) #序列号
x=scan[:,2].reshape(n,n)
y=scan[:,3].reshape(n,n)
f5=f5.reshape(n,n)
for i in range(0,n/2):
	s[2*i+1]=np.flipud(s[2*i+1])
	x[2*i+1]=np.flipud(x[2*i+1])
	y[2*i+1]=np.flipud(y[2*i+1])
	f5[2*i+1]=np.flipud(f5[2*i+1])

#find maxvalue of beam5 
seq,lin,col,maxvalue=0,0,0,-40
for i in range(len(f5)):
	for j in range(len(f5)):
		if (maxvalue<f5[i,j]):
			maxvalue,lin,col,seq=f5[i,j],x[i,j],y[i,j],s[i,j]
		else:
			continue
if (filename=='2019-2m/2D_15mm_2m_01.dat'):
	xmin=lin-r2;xmax=lin+r2
	ymin=col-r2;ymax=col+r2
else:
	xmin=lin-r1;xmax=lin+r1
	ymin=col-r1;ymax=col+r1
print seq,lin,col,maxvalue
print xmin,xmax,ymin,ymax

#contour
plt.figure(num=1,figsize=(20,10))
a=plt.contourf(x,y,f5,cmap='jet');b=plt.contour(x,y,f5,cmap='jet');plt.colorbar(a)
plt.clabel(b,inline=True,fontsize=10);
#plt.grid();
plt.xlabel('x(mm)');plt.ylabel('y(mm)')
plt.axvline(xmin,color='k');plt.axvline(xmax,color='k');plt.axhline(ymin,color='k');plt.axhline(ymax,color='k')
#plt.legend([lin,col,xmin,xmax,ymin,ymax])
plt.show()