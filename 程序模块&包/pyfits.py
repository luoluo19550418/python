import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits                                      # We use fits to open the actual data file

from astropy.utils import data
#data.conf.remote_timeout = 60

from spectral_cube import SpectralCube

from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp

co_data = fits.open('1340+005U.fits')                            # Open the FITS file for reading
cube = SpectralCube.read(co_data)                                # Initiate a SpectralCube
hi_data.close()                                                  # Close the FITS file - we already read it in and don't need it anymore!
print(cube)                                                      # 查看cube头部信息
cube[300, :, :].quicklook()                                      # Slice the cube along the spectral axis, and display a quick image
cube[:, 75, 75].quicklook()                                      # Extract a single spectrum through the data cube

sub_cube = cube.spectral(-300. *u.km / u.s, 300. *u.km / u.s)    
