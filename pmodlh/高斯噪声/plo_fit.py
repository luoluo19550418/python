import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import func

#get信号
x=np.linspace(-300,300,600)
y=func.gaussian(x,9.776,0,5.259)
'''
#无噪声
popt,pcov=curve_fit(func.gaussian,x,y,[9.776,0,5.259]); a=popt[0];b=popt[1];c=popt[2]; y_fit=func.gaussian(x,a,b,c)
plt.figure(num=1,figsize=(16,8))
plt.subplot(1,3,1)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x,y,"k-",linewidth=1,label='origin')
plt.plot(x,y_fit,"r-",linewidth=1,label='fit')
plt.legend(loc='upper right')
plt.xlabel('channel)'); plt.ylabel('T(k)');
'''
#加噪声
y_chushi=y
y_noise=func.noise(y_chushi,9.776)+y_chushi
popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,0,5.259]); a=popt[0];b=popt[1];c=popt[2]; y_fit=func.gaussian(x,a,b,c)
plt.subplot(1,3,2)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x,y_noise,"k-",linewidth=1,label='origin')
plt.plot(x,y_fit,"r-",linewidth=1,label='fit')
plt.legend(loc='upper right')
plt.xlabel('channel'); plt.ylabel('T(k)');
'''
#画噪声图
#5
x=np.linspace(-300,300,600)
y=func.gaussian(x,9.776,0,5.259)
y_noise=func.noise(y,5)+y
popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,0,5.259]); a=popt[0];b=popt[1];c=popt[2]; y_fit=func.gaussian(x,a,b,c)
plt.subplot(1,3,3)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x,y_noise,"g-",linewidth=1,label='5SNR')
plt.legend(loc='upper right')
plt.xlabel('channel'); plt.ylabel('T(k)')
#10
y_noise=func.noise(y,15)+y
popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,0,5.259]); a=popt[0];b=popt[1];c=popt[2]; y_fit=func.gaussian(x,a,b,c)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x,y_noise,"r-",linewidth=1,label='10SNR')
plt.legend(loc='upper right')
#30
y_noise=func.noise(y,30)+y
popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,0,5.259]); a=popt[0];b=popt[1];c=popt[2]; y_fit=func.gaussian(x,a,b,c)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x,y_noise,"b-",linewidth=1,label='30SNR')
plt.legend(loc='upper right')
plt.savefig("duibi.png")
'''