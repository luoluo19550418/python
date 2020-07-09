import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits                                      # We use fits to open the actual data file

from astropy.utils import data
data.conf.remote_timeout = 60

from spectral_cube import SpectralCube

from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp

co_data = fits.open('1340+005U.fits')                            # Open the FITS file for reading
cube = SpectralCube.read(co_data)                                # Initiate a SpectralCube
co_data.close()                                                  # Close the FITS file - we already read it in and don't need it anymore!
print(cube)                                                      # 查看cube头部信息
cube[300, :, :].quicklook()                                      # Slice the cube along the spectral axis, and display a quick image
cube[:, 46, 46].quicklook()                                      # Extract a single spectrum through the data cube

lon_range = [133.75, 134.25] * u.deg                                   # Define desired latitude and longitude range
lat_range = [0.25, 0.75] * u.deg
sub_cube = cube.subcube(xlo=lon_range[0], xhi=lon_range[1], ylo=lat_range[0], yhi=lat_range[1])          # Create a sub_cube cut to these coordinates
sub_cube_slab = sub_cube.spectral_slab(-100. *u.km / u.s, 100. *u.km / u.s)                              # Cut along the Spectral Axis
