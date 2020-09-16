def plohist(filec, num_bin, xlabel):
	dataset=pd.read_csv(path+filec,header=None,sep=' +',engine='python'); counts=[]; counts.extend(dataset.values[:,0]);
	fig=plt.figure(figsize=(15,10),dpi=80); ax1=fig.add_subplot(111); ax2=ax1.twinx()
	myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=30) #标签字体
	mpl.rcParams.update({'font.size': 20}) # 改变刻度所有字体大小，改变其他性质类似
	mpl.rcParams['xtick.direction'] = 'in'
	mpl.rcParams['ytick.direction'] = 'in'
	n, bins, patches = ax1.hist(counts, num_bin, rwidth=5, color='cyan', edgecolor='black', hatch='///', label="counts",); ax1.legend(loc='upper left')
#	ax1.set_xticks(bins,rotation=60)
	ax1.set_xlabel(xlabel); ax1.set_ylabel('counts');
	acc = [sum(n[:i])/len(counts) for i in range(len(n)+1)]
	ax2.plot(bins, acc, 'ro-', color='red', label="CDF"); ax2.legend(loc='upper right'); 
	ax2.set_ylabel('CDF(%)'); ax2.set_ylim(0,1.1); #ax2.set_xlim(xlim1,xlim2);
	ax2.grid(color='grey',linestyle='-.')
	plt.savefig(path+xlabel[0:3]+'.png')
#	plt.show()
#	return n,bins,patches
plohist('bPwv.dat', 22, 'PWV(mm)')

#参考：https://blog.csdn.net/qq_37948866/article/details/104102877
