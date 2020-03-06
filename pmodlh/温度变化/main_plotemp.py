#调用：findfolder.py finddir.py foreadfile.py plotdata.py
import findfolder
import finddir
import foreadfile
import plotdata

def everyfig():  #get一年一张图
	aa=findfolder.FindFolder('E:\code\python\plotTemp'); folder=aa.returnfolder()
	for i in folder:
		bb=finddir.FindDir(i+'\\'); listdir=bb.returndir()
		cc=foreadfile.ForeadFile(i+'\\',listdir); dt,a20,a21=cc.returndata()
		dd=plotdata.PlotData(dt,a20,a21,i[-7:]); dd.returnplot()

def comparefig():  #历年对比
	import pandas as pd
	import datetime
	import time
	import matplotlib
	import matplotlib.pyplot as plt
	import numpy as np
	myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
	color=['k','r','g','cyan','b','deeppink']
	fig=plt.figure(figsize=(25,15),facecolor='yellow')
	ax1=fig.add_subplot(2,1,1); ax2=fig.add_subplot(212)
	matplotlib.rcParams['xtick.direction']='in'
	matplotlib.rcParams['ytick.direction']='in'
	aa=findfolder.FindFolder('E:\code\python\plotTemp'); folder=aa.returnfolder()
	for j in range(len(folder)):
		bb=finddir.FindDir(folder[j]+'\\'); listdir=bb.returndir()
		cc=foreadfile.ForeadFile(folder[j]+'\\',listdir); dt,a20,a21=cc.returndata()
		#dtt=pd.to_datetime(dt); dttt=list(dtt.strftime("%m-%d"))  #时间处理
		ax1.plot(a20,color=color[j],lw=0.5,ls='-',label=folder[j][-7:]); ax1.legend()
		ax2.plot(a21,color=color[j],lw=1,ls='-',label=folder[j][-7:]); ax2.legend()
	ax1.set_xticks([])
	ax1.set_ylim(ymin=2.5,ymax=4.5)
	ax1.locator_params('y',nbins=10)
	ax1.set_xlabel('Date')
	ax1.set_ylabel('T(K)_4K')
	ax1.set_title('历年2月份接收机4K冷板温度变化',fontproperties=myfont)
	ax1.grid(linestyle='-.')
	ax2.grid(linestyle='-.')
	ax2.set_xticks([])
	ax2.set_xlabel('Date')
	ax2.set_ylabel('T(K)_50K')
	ax2.set_title('历年2月份接收机50K冷板温度变化',fontproperties=myfont)
	plt.savefig('comparefig.png')
	plt.show()

if __name__ == '__main__':
	everyfig()
	comparefig()



