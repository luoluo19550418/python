
import numpy as np
import matplotlib.pyplot as plt

#无噪声
v_fitwz=[]
with open('abc_wz.dat','r') as f:
	lines=f.readlines()
	for line in lines:
		value=[float(s) for s in line.split()]
		v_fitwz.append(value[1])
v_deltawz=[]
for i in range(0,600):
	v_deltawz.append(v_fitwz[i]-15.4)
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11=0,0,0,0,0,0,0,0,0,0,0   #get区间值数量
for i in range(0,600):
	if v_deltawz[i]<=-0.45:
		n1=n1+1
	elif -0.45<v_deltawz[i]<=-0.35:
		n2=n2+1
	elif -0.35<v_deltawz[i]<=-0.25:
		n3=n3+1
	elif -0.25<v_deltawz[i]<=-0.15:
		n4=n4+1
	elif -0.15<v_deltawz[i]<=-0.05:
		n5=n5+1
	elif -0.05<v_deltawz[i]<=0.05:
		n6=n6+1
	elif 0.05<v_deltawz[i]<=0.15:
		n7=n7+1
	elif 0.15<v_deltawz[i]<=0.25:
		n8=n8+1
	elif 0.25<v_deltawz[i]<=0.35:
		n9=n9+1
	elif 0.35<v_deltawz[i]<=0.45:
		n10=n10+1
	elif 0.45<v_deltawz[i]:
		n11=n11+1
print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)
n1=n1/600.0;n2=n2/600.0;n3=n3/600.0;n4=n4/600.0;n5=n5/600.0;n6=n6/600.0;n7=n7/600.0;n8=n8/600.0;n9=n9/600.0;n10=n10/600.0;n11=n11/600.0
wz_error=[-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
plt.figure(num=1,figsize=(20,10));plt.rcParams['xtick.direction'] = 'in';plt.rcParams['ytick.direction'] = 'in'
plt.subplot(131)
plt.bar(x,y,width=0.95)
plt.xticks(x,wz_error,fontsize=7)
plt.xlabel('error_channel'); plt.ylabel('percent(%)')

#不同噪声
v_fitsj=[]
with open('abc_sj.dat','r') as f:
	lines=f.readlines()
	for line in lines:
		value=[float(s) for s in line.split()]
		v_fitsj.append(value[1])
v_deltasj=[]
for i in range(0,600):
	v_deltasj.append(v_fitsj[i]-15.4)
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11=0,0,0,0,0,0,0,0,0,0,0   #get区间值数量
for i in range(0,600):
	if v_deltasj[i]<=-0.45:
		n1=n1+1
	elif -0.45<v_deltasj[i]<=-0.35:
		n2=n2+1
	elif -0.35<v_deltasj[i]<=-0.25:
		n3=n3+1
	elif -0.25<v_deltasj[i]<=-0.15:
		n4=n4+1
	elif -0.15<v_deltasj[i]<=-0.05:
		n5=n5+1
	elif -0.05<v_deltasj[i]<=0.05:
		n6=n6+1
	elif 0.05<v_deltasj[i]<=0.15:
		n7=n7+1
	elif 0.15<v_deltasj[i]<=0.25:
		n8=n8+1
	elif 0.25<v_deltasj[i]<=0.35:
		n9=n9+1
	elif 0.35<v_deltasj[i]<=0.45:
		n10=n10+1
	elif 0.45<v_deltasj[i]:
		n11=n11+1
print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)
n1=n1/600.0;n2=n2/600.0;n3=n3/600.0;n4=n4/600.0;n5=n5/600.0;n6=n6/600.0;n7=n7/600.0;n8=n8/600.0;n9=n9/1000.0;n10=n10/600.0;n11=n11/600.0
sj_error=[-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
plt.subplot(132)
plt.bar(x,y,width=0.95)
plt.xticks(x,sj_error,fontsize=7)
plt.xlabel('error_channel'); plt.ylabel('percent(%)')

#不同信噪比
v_fitxz=[]
with open('abc_xz.dat','r') as f:
	lines=f.readlines()
	for line in lines:
		value=[float(s) for s in line.split()]
		v_fitxz.append(value[1])
v_deltaxz=[]
for i in range(0,600):
	v_deltaxz.append(v_fitxz[i]-15.4)
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11=0,0,0,0,0,0,0,0,0,0,0   #get区间值数量
for i in range(0,600):
	if v_deltaxz[i]<=-0.45:
		n1=n1+1
	elif -0.45<v_deltaxz[i]<=-0.35:
		n2=n2+1
	elif -0.35<v_deltaxz[i]<=-0.25:
		n3=n3+1
	elif -0.25<v_deltaxz[i]<=-0.15:
		n4=n4+1
	elif -0.15<v_deltaxz[i]<=-0.05:
		n5=n5+1
	elif -0.05<v_deltaxz[i]<=0.05:
		n6=n6+1
	elif 0.05<v_deltaxz[i]<=0.15:
		n7=n7+1
	elif 0.15<v_deltaxz[i]<=0.25:
		n8=n8+1
	elif 0.25<v_deltaxz[i]<=0.35:
		n9=n9+1
	elif 0.35<v_deltaxz[i]<=0.45:
		n10=n10+1
	elif 0.45<v_deltaxz[i]:
		n11=n11+1
print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)
n1=n1/600.0;n2=n2/600.0;n3=n3/600.0;n4=n4/600.0;n5=n5/600.0;n6=n6/600.0;n7=n7/600.0;n8=n8/600.0;n9=n9/600.0;n10=n10/600.0;n11=n11/600.0
xz_error=[-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
plt.subplot(133)
plt.bar(x,y,width=0.95)
plt.xticks(x,xz_error,fontsize=7)
plt.xlabel('error_channel)'); plt.ylabel('percent(%)')
#plt.show()
plt.savefig('plo_hist.png')
