import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits                                      # We use fits to open the actual data file
from astropy.utils import data
from spectral_cube import SpectralCube
from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp
data.conf.remote_timeout = 60

#画图要用
myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=30) #标签字体
mpl.rcParams.update({'font.size': 20}) # 改变刻度所有字体大小，改变其他性质类似
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'

co_data = fits.open('1340+005U.fits')                            # Open the FITS file for reading
cube = SpectralCube.read(co_data)                                # Initiate a SpectralCube
co_data.close()                                                  # Close the FITS file - we already read it in and don't need it anymore!
#print(cube)                                                      # 查看cube头部信息
#cube[9001, :, :].quicklook(); plt.show()                                      # Slice the cube along the spectral axis, and display a quick image
#cube[:, 46, 46].quicklook(); plt.show()                                      # Extract a single spectrum through the data cube
##or plt.plt(cube[:, 46, 46])

lon_range = [133.75, 134.25] * u.deg                                   # Define desired latitude and longitude range
lat_range = [0.25, 0.75] * u.deg
sub_cube = cube.subcube(xlo=lon_range[0], xhi=lon_range[1], ylo=lat_range[0], yhi=lat_range[1])          # Create a sub_cube cut to these coordinates
sub_cube_slab = sub_cube.spectral_slab(-100. *u.km / u.s, 100. *u.km / u.s)                              # Cut along the Spectral Axis
sub_cube_slab[:,31,31].quicklook(); #plt.show() #为什么第一次画出错？后面又好了？
sub_cube_slab[:,31,31].quicklook()
plt.xticks(range(-100000,100000,20000),range(-100,100,20))
plt.xlabel('V(m/s)')
plt.ylabel('T(K)')
plt.title('12CO of (134,5)')
plt.show()
