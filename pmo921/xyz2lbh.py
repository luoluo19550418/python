# -*- coding: UTF-8 -*-
import math

def main():
    filename='/home/res/user/csluo/pmo921_csluo/orbit.txt'
    jd,X,Y,Z=[],[],[],[]
    with open(filename,'r') as f:
        lines=f.readlines()
        for line in lines:
            value=[float(s) for s in line.split( )]
            jd.append(value[0])
            X.append(value[1])
            Y.append(value[2])
            Z.append(value[3])
    f.close()
    for i in range(len(jd)):
        x=X[i]*1000.0
        y=Y[i]*1000.0
        z=Z[i]*1000.0
        l,b,h=XYZ2LBH(x,y,z)
        with open('/home/res/user/csluo/pmo921_csluo/BLZ.txt','a+') as f:
            f.write(str(jd[i]))
            f.write(' ')
            f.write(str(l))
            f.write(' ')
            f.write(str(b))
            f.write(' ')
            f.write(str(h)+'\n')

def XYZ2LBH(X, Y, Z): 
    aAxis, bAxis, B, L, preB0, ll, N = 6378137.0, 6356752.314, 0.0, 0.0, 0.0, 0.0, 0.0 
    e1 = (math.pow(aAxis, 2) - math.pow(bAxis, 2)) / math.pow(aAxis, 2)
    e2 = (math.pow(aAxis, 2) - math.pow(bAxis, 2)) / math.pow(bAxis, 2)
    
    S = math.sqrt(math.pow(X, 2) + math.pow(Y, 2)) 
    L = math.fabs(math.acos(X/S))
    if Y>0:
        L = L 
    else: 
        L = 2*math.pi-L

    B = math.atan(Z/S)
    c = aAxis * aAxis / bAxis
  
    #迭代计算纬度
    while math.fabs(preB0 - B) >= 0.001:
        preB0 = B 
        ll = math.pow(math.cos(B), 2) * e2
        N = c / math.sqrt(1 + ll) 
        TanB = (Z + N * e1 * math.sin(B)) / S 
        B = math.atan(TanB)

    ll = math.pow(math.cos(B), 2)* e2
    N = c / math.sqrt(1 + ll) 
              
    H = Z / math.sin(B) - N * (1 - e1) 
    B = B * 180 / math.pi
    L = L * 180 / math.pi
    return L,B,H

main()
