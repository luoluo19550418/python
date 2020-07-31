scan=np.loadtxt('1m2D8mm-001.dat')
scan[:,6]=10*(np.log10(scan[:,6]))-85.8; f0=scan[:,6] #功率瓦换算为dB
