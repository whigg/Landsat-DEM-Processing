import subprocess
# import matplotlib.pyplot as plt
import sys
# sys.path
try:
	import matplotlib
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])

import matplotlib.pyplot as plt

try:
	import numpy as np
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

import numpy as np

# GDAL (ORG included w/ GDAL) FIONA RASTERIO PYPROJ manual installation

import gdal
import ogr
import fiona
from fiona.crs import from_epsg
import rasterio
import rasterio.plot
import pyproj

# IMPORTS FOR MAPPING
import rasterio
from rasterio.transform import from_origin
from rasterio.warp import reproject, Resampling
import matplotlib.pyplot as plt
from rasterio.transform import from_bounds, from_origin
from rasterio.warp import reproject, Resampling
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.merge import merge
from rasterio.plot import show

try:
	import scipy
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scipy'])

import scipy

try:
	import descartes
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'descartes'])

import descartes


# import cartopy.crs as ccrs


try:
	import shapely
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'shapely'])

import shapely

from shapely.geometry import shape

# DOWNLOAD MAPS

try:
	import pandas
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

import pandas as pd

try:
	import geopandas as gpd
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'geopandas'])

import geopandas as gpd

try:
	import folium
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'folium'])

import folium

import os, shutil
from glob import glob
from os import listdir
# Import requests and beautiful soup
import requests

try:
	import bs4
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])

import bs4

from bs4 import BeautifulSoup

from shapely.geometry import Polygon 


import collections

# try:
# 	import landsatxplore
# except:
# 	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'landsatxplore'])

# import landsatxplore
# import landsatxplore.api
# from landsatxplore.earthexplorer import EarthExplorer

import datetime

import math

import urllib2,urllib

from os.path import exists

import copy
from copy import deepcopy

import tarfile
import tqdm

# from tqdm import tqdm

# try:
# 	import pci
# except:
# 	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pci'])

# import pci
# # import pci
# import pci.atcor
# from pci.atcor import *

#### For google ee
import re

try:
  # if setuptools is available, use it to take advantage of its dependency
  # handling
  from setuptools import setup                          # pylint: disable=g-import-not-at-top
except ImportError:
  # if setuptools is not available, use distutils (standard library). Users
  # will receive errors for missing packages
  from distutils.core import setup                      # pylint: disable=g-import-not-at-top
import ee
import ee.mapclient
from ee import batch
import time

