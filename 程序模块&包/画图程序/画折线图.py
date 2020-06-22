import matplotlib as mpl
import matplotlib.pyplot as plt

myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=20) #标签字体
mpl.rcParams.update({'font.size': 15}) # 改变刻度所有字体大小，改变其他性质类似

def ploline(x1,y1):
	plt.figure(num=1,figsize=(8,4))
	plt.plot(x1,y1)
	plt.xticks(x1)
	#plt.yticks(y1)
	plt.title('运行消耗费用',fontproperties=myfont)
	plt.xlabel('年份（年）',fontproperties=myfont)
	plt.ylabel('费用（万元）',fontproperties=myfont)
	#plt.savefig('运行消耗费用.png')
	plt.show()

x1=[2017,2018,2019]
y1=[14.7,14.67,13.2]
ploline(x1,y1)
