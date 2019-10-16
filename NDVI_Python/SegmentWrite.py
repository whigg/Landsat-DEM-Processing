# Imports for program
import Imports
from Imports import *


dir = 'ParsedLakeData'
if not os.path.exists(dir):
    os.makedirs(dir)

# New location for parsed lake segments
PLD = 'ParsedLakeData/'
SF_Dir = 'Shapefile/'

# Will write the file with a coordinate system
# LakeSeg = gpd.GeoDataFrame.from_file(SF_Dir+'LakeSeg.shp')
# f = gpd.GeoDataFrame.from_file(SF_Dir+'ParsedLake.shp')
# LakeSeg = LakeSeg.to_crs(f.crs)
# LakeSeg.to_file('LakeSeg.shp')
# sys.exit()

i = 0
# Will write individual shapefiles for each segment
with fiona.open(SF_Dir+'LakeSeg.shp') as File:
# with fiona.open(SF_Dir+'ParsedLake.shp') as File:
	# schema = File.schema
	meta = File.meta
	# print meta
	# sys.exit()
	for feature in File:
		# Define the feature id to define the number of segment for shp file
		Number = i
		# Write folders for all the data
		dir = 'ParsedLakeData/Segment'+str(Number)
		if not os.path.exists(dir):
			os.makedirs(dir)
		TempDir = 'ParsedLakeData/Segment'+str(Number)+'/'
		# Write the shapefile
		# with fiona.open(TempDir+str(Number)+'SegShp', 'w', crs=from_epsg(26914), driver='ESRI Shapefile', schema=schema) as output:
		with fiona.open(TempDir+str(Number)+'SegShp', 'w', **meta) as output:
				output.write(feature)
		i = i+1




