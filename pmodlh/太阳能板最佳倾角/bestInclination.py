import totalRadiation as tr

def INC(step, lloc=97, psi=37, Istart=0, Iend=91): #args 倾角步长，当地经度，当地纬度，倾角始末
	inc, yr = [], []
	for i in range(Istart, Iend, step): #beta
		sum = 0
		for j in range(1, 366, 1):
			for k in range(1, 25, 1):
				Gt= tr.Gt(i, j, k, lloc, psi)/1000 #W*h to kW*h
				if Gt>0: sum = sum + Gt
		inc.append(i)
		yr.append(sum)
	maxyr = max(yr)
	maxinc = inc[yr.index(maxyr)]
	return inc, yr, maxinc, maxyr