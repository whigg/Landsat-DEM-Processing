import subprocess
import sys
import os
import os, shutil
import glob
from glob import glob
from os import listdir
from os.path import exists
import math

try:
	import numpy as np
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

import numpy as np

try:
	import pandas as pd
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

import pandas as pd

import fiona

try:
	import tqdm
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])

import tqdm

try:
	import geopandas as gpd
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'geopandas'])

import geopandas as gpd
from geopandas import GeoDataFrame

try:
	import shapely
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'shapely'])

import shapely

from shapely import geometry
from shapely.geometry import shape
from shapely.geometry import Polygon, mapping
from shapely.geometry import Point