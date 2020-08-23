一、数学运算：
1、合数组
a=array([[ 1,  2],
         [ 3,  4]])
b=array([[ 2,  2],
         [ 2,  2]]) 
c=np.vstack((a,b)) #垂直
d=np.hstack((a,b)) #水平

2、
e=a.tolist() #数组转列表
f=np.array(e) #列表转数据

3、
a = np.zeros((437647,18))
a[:,1]=dataset.values[:,1] #把 dataset第一列值 赋值给 数组a的第一列

4、
list(map(lambda x: int(x),years)) #字符串型列表 转 整型列表
def s2f(sdata):
	fdata=[]
	for s in sdata:
		fdata.append(float(s))
	return fdata

5、异常处理
6、arr = np.empty((len(months),4),dtype=object); #定义空矩阵，可添字符串，浮点型等元素

