import numpy as np
import matplotlib.pyplot as plt

v_fitsj=[]
with open('abc_sj.dat','r') as f:
	lines=f.readlines()
	for line in lines:
		value=[float(s) for s in line.split()]
		v_fitsj.append(value[1])
v_deltasj=[]
for i in range(0,80):
	v_deltasj.append(v_fitsj[i]-15.4)
plt.subplot(3,1,2)
plt.plot(x,v_deltasj,"r-",linewidth=0.5,label='noise_plus');plt.legend(loc='upper right')
plt.xlabel('point'); plt.ylabel('error_channel')

