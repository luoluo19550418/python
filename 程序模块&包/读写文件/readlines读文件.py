#读单个文件

def returndata2(filename):
	data1,data2,data3,data4=[],[],[],[]  #可以添加识别几个参数
	with open(filename,'r') as f:
		lines=f.readlines()
		for line in lines:
			value=[s for s in line.split( )]
			data1.append(str(value[0])) #根据数据类型确定 str float。
			data2.append(str(value[1]))
			data3.append(float(value[20]))
			data4.append(float(value[21]))
	return data1,data2,data3,data4

data1,data2,data3,data4 = returndata2('./2020.02/record20200211.txt')


#读取多个文件（1个文件列表），追加到1个时间列表和1个数据列表
def returndata(listdir): #listdir is 所要读取的文件列表
	data1,data2,data3,data4=[],[],[],[]  #可以添加识别几个参数
	for i in listdir:
		with open(i,'r') as f:
			lines=f.readlines()
			for line in lines:
				value=[s for s in line.split( )]
				data1.append(float(value[0]))
				data2.append(float(value[1]))
				data3.append(float(value[20]))
				data4.append(float(value[21]))
	return data1,data2,data3,data4

data1,data2,data3,data4 = returndata(listdir)
