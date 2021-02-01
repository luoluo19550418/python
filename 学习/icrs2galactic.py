#赤道坐标转银道坐标系
#! /usr/local/bin/python3

import numpy as np
from astropy.coordinates import SkyCoord

if __name__ == "__main__":
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    
    ra_array = np.zeros((len(lines) ,1))
    dec_array = np.zeros((len(lines) ,1))

    for idx, line in enumerate(lines):
        line = line.split(' ')
        while True:
            try:
                line.remove('')
            except ValueError:
                break
        ra, dec, *_ = line
        ra_array[idx] = np.float(ra)
        dec_array[idx] = np.float(dec)
        
    c_obj = SkyCoord(ra=ra_array, dec=dec_array, frame='icrs', unit='deg')
    g = c_obj.galactic
    l = g.l.value
    b = g.b.value
    for i in range(len(l)):
        fmt = '{:6.9} {:6.9}'
        print(fmt.format(l[i][0], b[i][0]))
