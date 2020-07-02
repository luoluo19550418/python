import os
import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

beam=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# theoretical value
for line in open('rms0.dat'):
  rms0=float(line)

def dir_find_str(path,str): #pan duan wen jian
  numline=[]
  file_list=os.listdir(path)
  for filename in file_list:
    if os.path.isdir(filename):
      pass
    else:
      if str in filename:
        for line in open(filename):
          numline.append(line[0:-2])
  return numline

path=sys.argv[1]
numline=dir_find_str(path,'numline_')
numline=[int(n) for n in numline]
numline.sort(reverse=False)

rmsthe=[]
for i in range(len(beam)):
  rmsthe.append(3*rms0/np.sqrt(numline[i]))
# actual value
rms=[]
with open('rms.dat','r') as fr:
  lines=fr.readlines()
  for line in lines:
    value=[float(s) for s in line.split( )]
    rms.append(value[0])

# plo
plt.plot(beam,rms,color='blue',marker='o',label='origin_rms')
plt.plot(beam,rmsthe,color='green',marker='o',label='theo_rms')
plt.legend(loc='upper right')
plt.xlabel('beamsize(arcmin)')
plt.ylabel('rms(K)')
plt.title('variation of rms with beamsize')
plt.savefig('rmsfit.png')
plt.savefig('rmsfit.ps')

