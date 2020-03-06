#画图
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
class PlotData():
	def __init__(self,dt,a20,a21,i):
		self.dt=dt; self.a20=a20; self.a21=a21; self.i=i
	def returnplot(self):
		fig=plt.figure(); ax1=fig.add_subplot(111); ax2=ax1.twinx()
		matplotlib.rcParams['xtick.direction'] = 'in'
		matplotlib.rcParams['ytick.direction'] = 'in'
		ax1.plot(self.dt,self.a20,color='b',lw=1.0,ls='-',label='4K')
		ax1.legend(loc='upper left')
		ax1.set_xlabel('Date')
		ax1.set_ylabel('T(K)_4K')
		ax1.set_ylim(2.5,5)
		ax2.plot(self.dt,self.a21,color='r',lw=1.0,ls='-',label='50k')
		ax2.legend(loc='upper right')
		ax2.set_ylabel('T(K)_50K')
		ax2.set_ylim(30,80)
		
		plt.title(self.i+'月份接收机4K/50K冷板温度变化',fontproperties=myfont)
		plt.grid(linestyle='-.')
		plt.gcf().autofmt_xdate()
		plt.savefig(self.i+'.png')
		plt.show()
		plt.close
