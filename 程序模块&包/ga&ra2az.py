# ga&ra2az.py
# 2021.01.07 by csluo

from astropy import units as u #单位
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy.coordinates import AltAz
import numpy as np
import matplotlib.pyplot as plt


#radec2galactic verify
c=SkyCoord('20:12:06.542 38:21:17.78', unit=(u.hourangle, u.deg))
print(c.galactic)


'''
#galactic2radec verify
gc=SkyCoord(l=229.5*u.degree, b=-0.5*u.degree, frame='galactic') #1235+340 123.5 34.0
print(gc.icrs.to_string('hmsdms'))
'''

'''
#某一UTC时刻
c=SkyCoord('12:50:56   41:08:08',unit=(u.hourangle,u.deg))
observing_time = Time('2020-01-05 20:50:00') #UTC时间，not北京时
dlh=EarthLocation(lon=97.369751 * u.deg, lat=37.377139 * u.deg, height=3000 * u.m)
aa=AltAz(location=dlh, obstime=observing_time)
print(c.transform_to(aa)) #方位俯仰与时间对应13.7m观测记录稍有差别，是因为本地时和北京时的差（+7.*小时）
'''

'''
#俯仰随UTC变化
c=SkyCoord('05:06:52 42:21:16', unit=(u.hourangle, u.deg))
dlh = EarthLocation(lon='97d43m46s', lat='37d22m40s', height=3171.1*u.m)
observing_time = Time('2020-01-05 00:00:00') #UTC
delta_hours = np.linspace(0, 24, 480)*u.hour
full_night_times = observing_time + delta_hours
full_night_aa_frames = AltAz(location=dlh, obstime=full_night_times)
full_night_aa_coos = c.transform_to(full_night_aa_frames)
plt.plot(delta_hours, full_night_aa_coos.alt)
plt.xlabel('UTC time(hours)')
plt.ylabel('EL(deg)')
plt.locator_params(nbins=24)
plt.title('EL variety with UTC')
plt.grid()
plt.tight_layout()
plt.show()
'''
