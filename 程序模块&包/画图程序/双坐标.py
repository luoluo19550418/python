dataset=pd.read_csv(path+'PWV.dat',header=None,sep=' +',engine='python');
pwv=[]; pwv.extend(dataset.values[:,0]);
dataset=pd.read_csv(path+'pers.dat',header=None,sep=' +',engine='python');
pers=[]; pers.extend(dataset.values[:,0]);
s=0; S=[];
for per in pers: s=s+per; S.append(s)
num_bin = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21];

fig=plt.figure(figsize=(15,10),dpi=80); ax1=fig.add_subplot(111); ax2=ax1.twinx()
myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=30) #标签字体
mpl.rcParams.update({'font.size': 20}) # 改变刻度所有字体大小，改变其他性质类似
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
ax1.hist(pwv, num_bin,color="blue",edgecolor="black",hatch='///',label="counts",); ax1.legend(loc='upper left')
ax1.set_xlabel('pwv(mm)');
plt.xticks(num_bin); plt.xlim(0,20); #为了解决x=0和y=0不重合
ax1.set_ylabel('counts'); #ax1.set_ylim(2.5,5)
ax2.plot(S, color='red', label="CDF"); ax2.legend(loc='upper right')
ax2.legend(loc='upper right')
ax2.set_ylabel('CDF(%)'); ax2.set_ylim(0,100);

#plt.title(self.i+'月份接收机4K/50K冷板温度变化',fontproperties=myfont)  #"self.i"引用变量
plt.grid(linestyle='-.')
#plt.gcf().autofmt_xdate()
plt.savefig(path+'pwv.png')
plt.show()
#plt.close
