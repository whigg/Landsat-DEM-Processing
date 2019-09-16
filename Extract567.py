import Modules
from Modules import *


with fiona.open("a_shapefile.shp") as input:
	meta = input.meta
	with fiona.open('a_shapefile2.shp', 'w',**meta) as output:
		for feature in input:
			if feature['properties']['NAME']== name_dm1:
				 output.write(feature)