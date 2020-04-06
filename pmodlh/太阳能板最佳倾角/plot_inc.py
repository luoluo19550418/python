import matplotlib.pyplot as plt
import bestInclination as bi
import matplotlib
myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

inc, yr, maxinc, maxyr = bi.INC(1)
maxinc, maxyr = str(maxinc), str(round(maxyr))
plt.figure(num=1,figsize=(20,10))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(inc, yr, color='b',lw=1.0,ls='-',label='Annual radiation')
plt.legend(loc='upper right')
plt.annotate("最佳倾角：" + maxinc + '$^{\circ}$', xy = (25,2300), xytext = (25,2300), fontproperties=myfont)
plt.annotate("最大年辐射总量：" + maxyr + ' $kW\cdot h/m^2$', xy = (25,2250), xytext = (25,2250), fontproperties=myfont)
plt.xlabel('倾斜角($ ^{\circ}$)', fontproperties=myfont)
plt.ylabel('倾斜面年太阳辐射总量($kW\cdot h/m^2$)', fontproperties=myfont) #latex支持$$
plt.title('德令哈倾斜面年太阳辐射总量随倾斜角变化', fontproperties=myfont)
plt.savefig('inc.png')
plt.show()