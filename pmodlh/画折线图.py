import matplotlib
import matplotlib.pyplot as plt

myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=15)

x1=[2017,2018,2019]
y1=[14.7,14.67,13.2]
plt.figure(num=1,figsize=(8,4))
plt.plot(x1,y1)
plt.xticks(x1)
#plt.yticks(y1)
plt.title('运行消耗费用',fontproperties=myfont)
plt.xlabel('年份（年）',fontproperties=myfont)
plt.ylabel('费用（万元）',fontproperties=myfont)
plt.savefig('运行消耗费用.png')
