import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=30) #标签字体
mpl.rcParams.update({'font.size': 20}) # 改变刻度所有字体大小，改变其他性质类似

#画柱状图
def plobar(N, index, values):
	plt.figure(num=1, figsize=(10, 10), dpi=80) # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
	mpl.rcParams['xtick.direction'] = 'in'
	mpl.rcParams['ytick.direction'] = 'in'
	xl = np.arange(N) # 包含每个柱子下标的序列
	width = 0.45 # 柱子的宽度
	p2 = plt.bar(xl, values, width, label="num", color=['r','b','g'], hatch='///') # 绘制柱状图, 每根柱子的颜色为['r''b''g']
	plt.xlabel('年份（年）', fontproperties=myfont)
	plt.ylabel('费用（万元）', fontproperties=myfont)
	plt.title('运行消耗费用', fontproperties=myfont) # 添加标题
	plt.xticks(xl,index) # 添加纵横轴的刻度
	plt.yticks(np.arange(0, 22, 2)) #自定义y轴刻度
	for a, b in zip(xl, values):
		plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=20) #柱状图上标注数值
	#plt.savefig('运行消耗费用.png')
	plt.show()

index=('2017','2018','2019') #x轴坐标刻度值
values = (14.7,14.67,13.2) #包含每个柱子对应值的序列
plobar(3, index, values) #N=3，柱子总数
