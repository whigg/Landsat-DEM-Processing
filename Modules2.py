# Imports required

import subprocess
import sys
import os
from os.path import exists

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

try:
	import pandas
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

import pandas as pd
# GDAL (ORG included w/ GDAL) FIONA RASTERIO PYPROJ manual installation

import gdal
import ogr
import fiona
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


import cartopy.crs as ccrs

try:
	import shapely
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'shapely'])

import shapely

from shapely import geometry
from shapely.geometry import shape
from shapely.geometry import Polygon, mapping

# DOWNLOAD MAPS
##################################################
try:
	import geopandas as gpd
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'geopandas'])

import geopandas as gpd


import os, shutil
import glob
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

import collections


import datetime

import math

import urllib2,urllib

from os.path import exists

import copy
from copy import deepcopy

import tarfile
import tqdm
# from tqdm import tqdm

# Used for adding the online basemap
try:
	import contextily as ctx
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'contextily'])
import contextily as ctx

import shapefile

import time

import zipfile

# '*** Please install the `scikit-image` package (instead of `skimage`) ***`
from skimage import measure

from geojson import LineString

from geopandas import GeoDataFrame
from shapely.geometry import Point, shape
import math

try:
	import xarray as xr
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xarray'])
import xarray as xr


from rasterio.warp import transform


from array import array


from affine import Affine

from osgeo import osr