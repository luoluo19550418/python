arr = np.zeros((length,7),dtype=list) #定义list型矩阵
np.savetxt('2015.dat', arr, fmt="%s", delimiter='   ') #数组arr保存为字符串型(%.2f 2位小数的浮点数)，用空格分隔，如果是 浮点型等，可在前面运算或矩阵定义时处理。
