def plnum(years,arr):
	label=['years','Tmax','Tmin','Rmax','Rmin','Pmax','Pmin']
	myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=20) #标签字体
	mpl.rcParams.update({'font.size': 10}) # 改变刻度所有字体大小，改变其他性质类似
	plt.figure(figsize=(10,8));
	mpl.rcParams['xtick.direction'] = 'in'
	mpl.rcParams['ytick.direction'] = 'in'
	for col in range(1,len(arr[0,:]),1):
		plt.subplot(int('32'+str(col))) #用字符串来引用变量 !!!
		plt.plot(years,arr[:,col],linestyle='-', marker='o',label=label[col])
		plt.legend(loc='upper right')
		plt.xticks(rotation=30)
	plt.suptitle('历年温湿压最大值/中值/最小值变化',fontproperties=myfont)
	plt.show()
plnum(years,arr)
