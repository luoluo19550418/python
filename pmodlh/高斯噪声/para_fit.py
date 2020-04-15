import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import func

#get信号
x=np.linspace(-300,300,600)
y=func.gaussian(x,9.776,15.4,5.259)

##############################################################################################
#不加噪声
for i in range(0,600):
	#nihe
	popt,pcov=curve_fit(func.gaussian,x,y,[9.776,15.4,5.259])
	A=popt[0];B=popt[1];C=popt[2]
	popt_list=popt.tolist()
	popt_num=" ".join(str(i) for i in popt_list)
	f=open('abc_wz.dat','a')
	f.write(popt_num)
	f.write('\n')
	f.close

#不同噪声(信噪比一定)
for i in range(0,600):
	y_noise=func.noise(y,9.776)+y
	#nihe
	popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,15.4,5.259])
	A=popt[0];B=popt[1];C=popt[2]
	popt_list=popt.tolist()
	popt_num=" ".join(str(i) for i in popt_list)          #以空格形式输出
	f=open('abc_sj.dat','a')
	f.write(popt_num)
	f.write('\n')
	#y_fit=gaussian(x,A,B,C)
	f.close

#不同信噪比(噪声变化)
for i in range(0,601):
	y_noise=func.noise(y,i)+y
	#nihe
	popt,pcov=curve_fit(func.gaussian,x,y_noise,[9.776,15.4,5.259])
	A=popt[0];B=popt[1];C=popt[2]
	popt_list=popt.tolist()
	popt_num=" ".join(str(i) for i in popt_list)
	f=open('abc_xz.dat','a')
	f.write(popt_num)
	f.write('\n')
	f.close