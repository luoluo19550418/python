import numpy as np
import matplotlib.pyplot as plt
import matplotlib

myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=25) #标签字体
matplotlib.rcParams.update({'font.size': 15}) # 改变刻度所有字体大小，改变其他性质类似

plt.figure(num=1, figsize=(10, 10), dpi=80) # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
N = 3 # 柱子总数
values = (14.7,14.67,13.2) # 包含每个柱子对应值的序列
index = np.arange(N) # 包含每个柱子下标的序列
width = 0.45 # 柱子的宽度
p2 = plt.bar(index, values, width, label="num", color=['r','b','g'], hatch='///') # 绘制柱状图, 每根柱子的颜色为紫罗兰色
plt.xlabel('年份（年）', fontproperties=myfont)
plt.ylabel('费用（万元）', fontproperties=myfont)
plt.title('运行消耗费用', fontproperties=myfont) # 添加标题
plt.xticks(index,('2017','2018','2019')) # 添加纵横轴的刻度
plt.yticks(np.arange(0, 22, 2))
for a, b in zip(index, values):
  plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=11) 
plt.savefig('运行消耗费用.png')

plt.figure(num=2, figsize=(10, 10), dpi=80) # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
N = 3 # 柱子总数
values = (739.38,855.04,832.58) # 包含每个柱子对应值的序列
index = np.arange(N) # 包含每个柱子下标的序列
width = 0.45 # 柱子的宽度
p2 = plt.bar(index, values, width, label="num", color=['r','b','g'], hatch='///') # 绘制柱状图, 每根柱子的颜色为紫罗兰色
plt.xlabel('年份（年）', fontproperties=myfont)
plt.ylabel('费用（万元）', fontproperties=myfont)
plt.title('人员费用', fontproperties=myfont) # 添加标题
plt.xticks(index,('2017','2018','2019')) # 添加纵横轴的刻度
plt.yticks(np.arange(0, 1200, 100))
for a, b in zip(index, values):
  plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=11) 
plt.savefig('人员费用.png')

plt.figure(num=3, figsize=(10, 10), dpi=80) # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
N = 3 # 柱子总数
values = (186.26,367.69,221.24) # 包含每个柱子对应值的序列
index = np.arange(N) # 包含每个柱子下标的序列
width = 0.45 # 柱子的宽度
p2 = plt.bar(index, values, width, label="num", color=['r','b','g'], hatch='///') # 绘制柱状图, 每根柱子的颜色为紫罗兰色
plt.xlabel('年份（年）', fontproperties=myfont)
plt.ylabel('费用（万元）', fontproperties=myfont)
plt.title('科研业务费用', fontproperties=myfont) # 添加标题
plt.xticks(index,('2017','2018','2019')) # 添加纵横轴的刻度
plt.yticks(np.arange(0, 500, 50))
for a, b in zip(index, values):
  plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=11) 
plt.savefig('科研业务费用.png')
