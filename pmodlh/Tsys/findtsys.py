#python2.7
#findtime.py

import os
import pandas as pd
import numpy as np
import datetime

def returndir(path, char):
  listdir=[]
  dirs=os.listdir(path)
  for file in dirs:
    if file[0:12]==char and file[14:18]==".txt":
      listdir.append(file)
  return listdir

def returntime(path, listdir):
  flist, elist, dlist, tlist, Tlist = [], [], [], [], [] 
  for file in listdir:
    timelist, ellist, freqlist, Tcallist = [], [], [], []
    datasetobs = pd.read_csv(path + file, header=None, sep=' +', engine='python')
    timelist.extend(datasetobs.values[:,1]); ellist.extend(datasetobs.values[:,9]); Tcallist.extend(datasetobs.values[:,12]); freqlist.extend(datasetobs.values[:,22])
    delta0, elbest, tmp1, tmp2, tmp3 = 0.100, 70.000, [], [], []
    for i in range(len(timelist)):
      if freqlist[i] == 112.67:  #judge freq
        if ellist[i] > 69.100 and ellist[i] < 70.100:
          delta1 = np.abs(ellist[i] - 70.000)
          if delta1 < delta0:
            elbest = ellist[i]
            timebest = timelist[i]
            delta0 = delta1
            tmp1.append(file); tmp2.append(timebest); tmp3.append(Tcallist[i])
    if len(tmp1)>0:
      flist.append(tmp1[-1]); tlist.append(tmp2[-1]); Tlist.append(tmp3[-1])
  return flist, tlist, Tlist

def returnIF(f, IFpath):
  year = f[6:10]; month = f[10:12]; day = f[12:14]
  filename = "IF"+year+"_"+month+"_"+day+".dat"
  ti, IF1, IF2, IF3, IF4, IF5, IF6, IF7, IF8, IF9, IF10, IF11, IF12, IF13, IF14, IF15, IF16, IF17, IF18  = [], [], [], [], [], [], [], [], [], [], [], [], [], [],[], [], [], [], []
  path = IFpath+filename
  if os.path.exists(path): 
    with open(IFpath+filename,'r') as fp:
      lines = fp.readlines()
      for line in lines:
        value = [ s for s in line.split()]
        ti.append(value[0])
        #print value[2]; print filename
        IF1.append(float(value[1])); IF2.append(float(value[2])); IF3.append(float(value[3])); IF4.append(float(value[4])); IF5.append(float(value[5])); IF6.append(float(value[6])); 
        #print value[7]; print filename; 
        IF7.append(float(value[7]));
        IF8.append(float(value[8])); 
        IF9.append(float(value[9])); 
        IF10.append(float(value[10])); 
        IF11.append(float(value[11])); 
        IF12.append(float(value[12])); 
        IF13.append(float(value[13])); IF14.append(float(value[14])); IF15.append(float(value[15])); IF16.append(float(value[16])); IF17.append(float(value[17])); IF18.append(float(value[18]))
  return ti, IF1, IF2, IF3, IF4, IF5, IF6, IF7, IF8, IF9, IF10, IF11, IF12, IF13, IF14, IF15, IF16, IF17, IF18

def returntsys(flist, tlist, Tlist, outfn, IFpath): #diao yong returnIF(f)

  path = outfn
  if os.path.exists(path):
    os.remove(outfn)
  else:
    print ("no such file: %s" %outfn)

  tsys1, tsys2, tsys3, tsys4, tsys5, tsys6, tsys7, tsys8, tsys9 = [], [], [], [], [], [], [], [], []
  tsys10, tsys11, tsys12, tsys13, tsys14, tsys15, tsys16, tsys17, tsys18 = [], [], [], [], [], [], [], [], []
  for i in range(len(flist)):
    fd = flist[i]; tb = tlist[i]; Tcal = Tlist[i]
    if tb > "00:03:00" and tb < "23:57:00":
      tmin = (datetime.datetime.strptime(tb, '%H:%M:%S') + datetime.timedelta(minutes=-3)).strftime("%H:%M:%S")
      tmax = (datetime.datetime.strptime(tb, '%H:%M:%S') + datetime.timedelta(minutes=3)).strftime("%H:%M:%S")
      ti, IF1, IF2, IF3, IF4, IF5, IF6, IF7, IF8, IF9, IF10, IF11, IF12, IF13, IF14, IF15, IF16, IF17, IF18 = returnIF(flist[i], IFpath)
      #print ti, IF1, IF2, IF3, IF4, IF5, IF6, IF7, IF8, IF9, IF10, IF11, IF12, IF13, IF14, IF15, IF16, IF17, IF18
      S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
      B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
      for j in range(len(ti)):
        if tmin < ti[j] < tmax:
          if float(IF1[j]) < -6:
            S1.append(IF1[j]); S2.append(IF2[j]); S3.append(IF3[j]); S4.append(IF4[j]); S5.append(IF5[j]); S6.append(IF6[j]); S7.append(IF7[j]); S8.append(IF8[j]); S9.append(IF9[j])
            S10.append(IF10[j]); S11.append(IF11[j]); S12.append(IF12[j]); S13.append(IF13[j]); S14.append(IF14[j]); S15.append(IF15[j]); S16.append(IF16[j]); S17.append(IF17[j]);S18.append(IF18[j])
          else:
            B1.append(IF1[j]); B2.append(IF2[j]); B3.append(IF3[j]); B4.append(IF4[j]); B5.append(IF5[j]); B6.append(IF6[j]); B7.append(IF7[j]); B8.append(IF8[j]); B9.append(IF9[j])
            B10.append(IF10[j]); B11.append(IF11[j]); B12.append(IF12[j]); B13.append(IF13[j]); B14.append(IF14[j]); B15.append(IF15[j]); B16.append(IF16[j]); B17.append(IF17[j]);B18.append(IF18[j])
      #print fd,tb,S1,B2,B3,B4
      ps1 = 10**(( S1[len(S1)/2] )/10); ps2 = 10**(( S2[len(S2)/2] )/10); ps3 = 10**(( S3[len(S3)/2] )/10); ps4 = 10**(( S4[len(S4)/2] )/10);
      ps5 = 10**(( S5[len(S5)/2] )/10); ps6 = 10**(( S6[len(S6)/2] )/10); ps7 = 10**(( S7[len(S7)/2] )/10); ps8 = 10**(( S8[len(S8)/2] )/10);
      ps9 = 10**(( S9[len(S9)/2] )/10); ps10 = 10**(( S10[len(S10)/2] )/10); ps11 = 10**(( S11[len(S11)/2] )/10); ps12 = 10**(( S12[len(S12)/2] )/10); ps13 = 10**(( S13[len(S13)/2] )/10); 
      ps14 = 10**(( S14[len(S14)/2] )/10); ps15 = 10**(( S15[len(S15)/2] )/10); ps16 = 10**(( S16[len(S16)/2] )/10); ps17 = 10**(( S17[len(S17)/2] )/10); ps18 = 10**(( S18[len(S18)/2] )/10)
      #print fd,tb,ps13,ps14,ps15,ps16,ps17,ps18
      if len(B1)>0 and len(B2)>0 and len(B3)>0 and len(B4)>0 and len(B5)>0 and len(B6)>0 and len(B7)>0 and len(B8)>0 and len(B9)>0 and len(B10)>0 and len(B11)>0 and len(B12)>0 and len(B13)>0 and len(B14)>0 and len(B15)>0 and len(B16)>0 and len(B17)>0 and len(B18)>0:
        pb1 = 10**(( B1[len(B1)/2] )/10); pb2 = 10**(( B2[len(B2)/2] )/10); pb3 = 10**(( B3[len(B3)/2] )/10); pb4 = 10**(( B4[len(B4)/2] )/10);
        pb5 = 10**(( B5[len(B5)/2] )/10); pb6 = 10**(( B6[len(B6)/2] )/10); pb7 = 10**(( B7[len(B7)/2] )/10); pb8 = 10**(( B8[len(B8)/2] )/10);
        pb9 = 10**(( B9[len(B9)/2] )/10); pb10 = 10**(( B10[len(B10)/2] )/10); pb11 = 10**(( B11[len(B11)/2] )/10); pb12 = 10**(( B12[len(B12)/2] )/10); pb13 = 10**(( B13[len(B13)/2] )/10);
        pb14 = 10**(( B14[len(B14)/2] )/10); pb15 = 10**(( B15[len(B15)/2] )/10); pb16 = 10**(( B16[len(B16)/2] )/10); pb17 = 10**(( B17[len(B17)/2] )/10); pb18 = 10**(( B18[len(B18)/2] )/10)
        #print pb13,pb14,pb15,pb16,pb17,pb18
        if pb1 != ps1:  
          tsys1=round(Tcal/(pb1/ps1-1),1)
        else: tsys1=0
        if pb2 != ps2: 
          tsys2=round(Tcal/(pb2/ps2-1),1)
        else: tsys2=0
        if pb3 != ps3:
          tsys3=round(Tcal/(pb3/ps3-1),1)
        else: tsys3=0
        if pb4 != ps4:
          tsys4=round(Tcal/(pb4/ps4-1),1)
        else: tsys4=0
        if pb5 != ps5:
          tsys5=round(Tcal/(pb5/ps5-1),1)
        else: tsys5=0
        if pb6 != ps6:
          tsys6=round(Tcal/(pb6/ps6-1),1)
        else: tsys6=0
        if pb7 != ps7:
          tsys7=round(Tcal/(pb7/ps7-1),1)
        if pb8 != ps8:
          tsys8=round(Tcal/(pb8/ps8-1),1);
        else: tsys8=0
        if pb9 != ps9:
          tsys9=round(Tcal/(pb9/ps9-1),1)
        else: tsys9=0
        if pb10 != ps10:
          tsys10=round(Tcal/(pb10/ps10-1),1)
        else: tsys10=0
        if pb11 != ps11:
          tsys11=round(Tcal/(pb11/ps11-1),1)
        else: tsys11=0
        if pb12 != ps12:  
          tsys12=round(Tcal/(pb12/ps12-1),1)
        else: tsys12=0
        if pb13 != ps13: 
           tsys13=round(Tcal/(pb13/ps13-1),1); 
        else: tsys13=0
        if pb14 != ps14:      
          tsys14=round(Tcal/(pb14/ps14-1),1)
        else: tsys14=0
        if pb15 != ps15:
          tsys15=round(Tcal/(pb15/ps15-1),1)
        else: tsys15=0
        if pb16 != ps16:
          tsys16=round(Tcal/(pb16/ps16-1),1)
        else: tsys16=0
        if pb17 != ps17:
          tsys17=round(Tcal/(pb17/ps17-1),1)
        else: tsys17=0
        if pb18 != ps18:
          tsys18=round(Tcal/(pb18/ps18-1),1) 
        else: tsys18=0
        #tsysU=(tsys1+tsys3+tsys5+tsys7+tsys9+tsys11+tsys13+tsys15+tsys17)/9; tsysL=(tsys2+tsys4+tsys6+tsys8+tsys10+tsys12+tsys14+tsys16+tsys18)/9; print fd,tb,tsysU,tsysL
        #return fd[6:14], tb, tsys1, tsys2, tsys3, tsys4, tsys5, tsys6, tsys7, tsys8, tsys9,tsys10, tsys11, tsys12, tsys13, tsys14, tsys15, tsys16, tsys17, tsys18  
        
        with open(outfn,'a') as f:
          f.write(fd[6:14]); f.write(" "); f.write(tb); f.write(" "); f.write(str(tsys1)); f.write(" "); f.write(str(tsys3)); f.write(" "); f.write(str(tsys5)); f.write(" "); f.write(str(tsys7));
          f.write(" "); f.write(str(tsys9)); f.write(" "); f.write(str(tsys11)); f.write(" "); f.write(str(tsys13)); f.write(" "); f.write(str(tsys15)); f.write(" "); f.write(str(tsys17));
          f.write(" "); f.write(str(tsys2)); f.write(" "); f.write(str(tsys4)); f.write(" "); f.write(str(tsys6)); f.write(" "); f.write(str(tsys8)); f.write(" "); f.write(str(tsys10)); f.write(" "); 
          f.write(str(tsys12)); f.write(" "); f.write(str(tsys14)); f.write(" "); f.write(str(tsys16)); f.write(" "); f.write(str(tsys18))
          f.write("\n"); f.close

listdir=returndir("/home/res/obsrecord/2011/", "record201112") 
flist, tlist, Tlist = returntime("/home/res/obsrecord/2011/", listdir)
#print flist
returntsys(flist, tlist, Tlist, "tsys201112.dat", "/home/res/becufecu/becu/2011/")
