# Imports required

import subprocess
import sys
import os


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

from shapely.geometry import shape

# DOWNLOAD MAPS

try:
	import pandas
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

import pandas as pd
##################################################
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

try:
	import landsatxplore
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'landsatxplore'])

import landsatxplore
import landsatxplore.api
from landsatxplore.earthexplorer import EarthExplorer

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