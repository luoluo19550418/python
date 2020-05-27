#plotsys.py
#shell python2.7

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def returndir(path):
  listdir=[]
  dirs=os.listdir(path)
  for file in dirs:
    if file[4:8]==".dat":
      listdir.append(file)
  return listdir

def returntsys(filename):
  tsys1,tsys2,tsys3,tsys4,tsys5,tsys6,tsys7,tsys8,tsys9,tsys10,tsys11,tsys12,tsys13,tsys14,tsys15,tsys16,tsys17,tsys18 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
  datasetobs = pd.read_csv(filename, header=None, sep=' +', engine='python')
  tsys1.extend(datasetobs.values[:,2]); tsys2.extend(datasetobs.values[:,3]); tsys3.extend(datasetobs.values[:,4]); tsys4.extend(datasetobs.values[:,5]); tsys5.extend(datasetobs.values[:,6]); 
  tsys6.extend(datasetobs.values[:,7]); tsys7.extend(datasetobs.values[:,8]); tsys8.extend(datasetobs.values[:,9]); tsys9.extend(datasetobs.values[:,10]); tsys10.extend(datasetobs.values[:,11]);
  tsys11.extend(datasetobs.values[:,12]); tsys12.extend(datasetobs.values[:,13]); tsys13.extend(datasetobs.values[:,14]); tsys14.extend(datasetobs.values[:,15]); 
  tsys15.extend(datasetobs.values[:,16]); tsys16.extend(datasetobs.values[:,17]); tsys17.extend(datasetobs.values[:,18]); tsys18.extend(datasetobs.values[:,19])
  return tsys1,tsys2,tsys3,tsys4,tsys5,tsys6,tsys7,tsys8,tsys9,tsys10,tsys11,tsys12,tsys13,tsys14,tsys15,tsys16,tsys17,tsys18 
  
def avetsys(listdir):
  U1,U2,U3,U4,U5,U6,U7,U8,U9,L1,L2,L3,L4,L5,L6,L7,L8,L9 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[] 
  for filename in listdir:
    #print filenam
    tsys1,tsys2,tsys3,tsys4,tsys5,tsys6,tsys7,tsys8,tsys9,tsys10,tsys11,tsys12,tsys13,tsys14,tsys15,tsys16,tsys17,tsys18 = returntsys(filename)
    usb1=round(np.mean(tsys1),1); usb2=round(np.mean(tsys2),1); usb3=round(np.mean(tsys3),1); usb4=round(np.mean(tsys4),1); usb5=round(np.mean(tsys5),1); usb6=round(np.mean(tsys6),1); usb7=round(np.mean(tsys7),1); usb8=round(np.mean(tsys8),1); usb9=round(np.mean(tsys9),1)
    lsb1=round(np.mean(tsys10),1); lsb2=round(np.mean(tsys11),1); lsb3=round(np.mean(tsys12),1); lsb4=round(np.mean(tsys13),1); lsb5=round(np.mean(tsys14),1); lsb6=round(np.mean(tsys15),1); lsb7=round(np.mean(tsys16),1); lsb8=round(np.mean(tsys17),1); lsb9=round(np.mean(tsys18),1)
    if usb1 > 100: U1.append(usb1)
    else: U1.append(0)
    if usb2 > 100: U2.append(usb2)
    else: U2.append(0)
    if usb3 > 100: U3.append(usb3)
    else: U3.append(0)
    if usb4 > 100: U4.append(usb4)
    else: U4.append(0)
    if usb5 > 100: U5.append(usb5)
    else: U5.append(0)
    if usb6 > 100: U6.append(usb6)
    else: U6.append(0)
    if usb7 > 100: U7.append(usb7)
    else: U7.append(0)
    if usb8 > 100: U8.append(usb8)
    else: U8.append(0)
    if usb9 > 100: U9.append(usb9)
    else: U9.append(0)

    if lsb1 > 50: L1.append(lsb1)
    else: L1.append(0)
    if lsb2 > 50: L2.append(lsb2)
    else: L2.append(0)
    if lsb3 > 50: L3.append(lsb3)
    else: L3.append(0)
    if lsb4 > 50: L4.append(lsb4)
    else: L4.append(0)
    if lsb5 > 50: L5.append(lsb5)
    else: L5.append(0)
    if lsb6 > 50: L6.append(lsb6)
    else: L6.append(0)
    if lsb7 > 50: L7.append(lsb7)
    else: L7.append(0)
    if lsb8 > 50: L8.append(lsb8)
    else: L8.append(0)
    if lsb9 > 50: L9.append(lsb9)
    else: L9.append(0)

  return U1,U2,U3,U4,U5,U6,U7,U8,U9,L1,L2,L3,L4,L5,L6,L7,L8,L9

def plotsys(U1,U2,U3,U4,U5,U6,U7,U8,U9,L1,L2,L3,L4,L5,L6,L7,L8,L9):
  x = [0,1,2,3,4,5,6,7,8]
  fig=plt.figure(figsize=(20,10))
  plt.subplot(121)
  matplotlib.rcParams['xtick.direction'] = 'in'
  matplotlib.rcParams['ytick.direction'] = 'in'
  plt.plot(U1,color='black',lw=1.0,ls='-',label='USB1')
  plt.plot(U2,color='b',lw=1.0,ls='-',label='USB2')
  plt.plot(U3,color='g',lw=1.0,ls='-',label='USB3')
  plt.plot(U4,color='orange',lw=1.0,ls='-',label='USB4')
  plt.plot(U5,color='r',lw=1.0,ls='-',label='USB5')
  plt.plot(U6,color='lime',lw=1.0,ls='-',label='USB6')
  plt.plot(U7,color='chocolate',lw=1.0,ls='-',label='USB7')
  plt.plot(U8,color='lightcyan',lw=1.0,ls='-',label='USB8')
  plt.plot(U9,color='purple',lw=1.0,ls='-',label='USB9')
  plt.legend(loc='lower right')
  plt.xlabel('years')
  plt.ylabel('Tsys(K)')
  #ax1.set_ylim(0,300)
  plt.title('Tsys of USB over the years')
  plt.xticks(x,('2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'))
  plt.grid(linestyle='-.')

  plt.subplot(122)
  matplotlib.rcParams['xtick.direction'] = 'in'
  matplotlib.rcParams['ytick.direction'] = 'in'
  plt.plot(L1,color='black',lw=1.0,ls='-',label='LSB1')
  plt.plot(L2,color='b',lw=1.0,ls='-',label='LSB2')
  plt.plot(L3,color='g',lw=1.0,ls='-',label='LSB3')
  plt.plot(L4,color='orange',lw=1.0,ls='-',label='LSB4')
  plt.plot(L5,color='r',lw=1.0,ls='-',label='LSB5')
  plt.plot(L6,color='lime',lw=1.0,ls='-',label='LSB6')
  plt.plot(L7,color='chocolate',lw=1.0,ls='-',label='LSB7')
  plt.plot(L8,color='lightcyan',lw=1.0,ls='-',label='LSB8')
  plt.plot(L9,color='purple',lw=1.0,ls='-',label='LSB9')
  plt.legend(loc='lower right')
  plt.xlabel('years')
  plt.ylabel('Tsys(K)')
  #ax2.set_ylim(0,300)
  plt.title('Tsys of USB over the years')
  plt.xticks(x,('2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'))
  plt.grid(linestyle='-.')

  #plt.gcf().autofmt_xdate()
  plt.savefig('tsys.png')
  #plt.show()
 #plt.close

listdir = returndir("./")
#tsys1,tsys2,tsys3,tsys4,tsys5,tsys6,tsys7,tsys8,tsys9,tsys10,tsys11,tsys12,tsys13,tsys14,tsys15,tsys16,tsys17,tsys18 = returntsys("2011.dat")
U1,U2,U3,U4,U5,U6,U7,U8,U9,L1,L2,L3,L4,L5,L6,L7,L8,L9 = avetsys(listdir)
plotsys(U1,U2,U3,U4,U5,U6,U7,U8,U9,L1,L2,L3,L4,L5,L6,L7,L8,L9)
'''print U1
print U2
print U3
print U4
print U5
print U6
print U7
print U8
print U9
print L1
print L2
print L3
print L4
print L5
print L6
print L7
print L8
print L9'''
