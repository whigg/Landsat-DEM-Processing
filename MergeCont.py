# import Modules
# from Modules import *

import SubMod
from SubMod import *

dir = 'Merge_Contours'
if not os.path.exists(dir):
    os.makedirs(dir)
Out_Dir = 'Merge_Contours/'

dir = 'Merge_Contours/ParsedSHP'
if not os.path.exists(dir):
    os.makedirs(dir)
Parse_Dir = 'Merge_Contours/ParsedSHP/'

dir = 'Merge_Contours/CSV_Relate'
if not os.path.exists(dir):
    os.makedirs(dir)
ParseCSV_Dir = 'Merge_Contours/CSV_Relate/'


Shapefile = '567Contour.shp'

# Write a shapefile with buffers

ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
with fiona.open(Shapefile) as input:
	print '\nAdding Buffers...\n'
	ProgBarLimit = len(input)
	for i in tqdm.tqdm(range(ProgBarLimit)):
		Polygon = input[i]
		# Define the id for a given poly
		ID = int(Polygon['properties']['id'])
		Geom = Polygon['geometry']['coordinates'][0]
		Geom = tuple(Geom)
		from shapely.geometry import Polygon
		Po = Polygon(Geom)
		BFP = Po.buffer(0.1)
		InsertItem = [ID, BFP]
		TempDF = pd.DataFrame(InsertItem)
		# Rotate the data to match our desired format
		TempDF = TempDF.transpose()
		# Insert the column names
		TempDF.columns = ['id', 'geometry']
		ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)

# Convert the dataframe to a geodataframe
gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# No refrence system is in this file yet, we must set it to the correct one
# before changing it.
gdf.crs = fiona.crs.from_epsg(26914)
# Write a shapefile from the geodataframe object
print 'Writting the shapefile: 567WithBuff_.1.shp'
gdf.to_file("567WithBuff_.1.shp")

########################################################################


Shapefile = '567WithBuff_.1.shp'


# USE*** This will parse the larger file by thousands for easier iteration


ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
counter = 0
errorRec = []
FinalI = 0
with fiona.open(Shapefile) as input:
	print '\nParsing the shapefile...\n'
	ProgBarLimit = len(input)
	# ProgBarLimit = 3000
	for i in tqdm.tqdm(range(ProgBarLimit)):
		try:
			Polygon = input[i]
			# Define the id for a given poly
			ID = int(Polygon['properties']['id'])
			Geom = Polygon['geometry']['coordinates'][0]
			Geom = tuple(Geom)
			from shapely.geometry import Polygon
			Po = Polygon(Geom)
			InsertItem = [ID, Po]
		except:
			print 'Error with record attribute: %i' % i
			errorRec.append(i)
			pass
		try:
			if Po.is_valid==True:
				TempDF = pd.DataFrame(InsertItem)
				# Rotate the data to match our desired format
				TempDF = TempDF.transpose()
				# Insert the column names
				TempDF.columns = ['id', 'geometry']
				ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)
				counter = counter+1
				FinalI = i
		except:
			print 'Error with record True/False Handle: %i' % i
			errorRec.append(i)
			pass

		if counter==1000:
			# Convert the dataframe to a geodataframe
			gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
			gdf.crs = fiona.crs.from_epsg(26914)
			FileName = str(i+1)+'Iteration.shp'
			gdf.to_file(Parse_Dir+FileName)
			ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
			counter=0

if len(ShapeFileDF)!=0:
	# Convert the dataframe to a geodataframe
	gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
	gdf.crs = fiona.crs.from_epsg(26914)
	FileName = str(FinalI+1)+'Iteration.shp'
	gdf.to_file(Parse_Dir+FileName)

# print 'Force Finishe here for now...'
# sys.exit()

#######################################################################


# Open parsed dataset piece by piece for comparison

# Write list of shapefiles in directory
ParsedShapes = []
for file in os.listdir(Parse_Dir):
    if file.endswith(".shp"):
        ParsedShapes.append(Parse_Dir+file)

# Each list item will consist of sublists of relations between 2 items
# Relations = []

# ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
MasterDF = pd.DataFrame(columns=['id_left', 'id_right'])
ProgBarLimit = len(ParsedShapes)
for i in tqdm.tqdm(range(ProgBarLimit)):
	ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
	# Open file to be compaired with
	with fiona.open(ParsedShapes[i]) as input:
		# Extract the polygons from the file
		for aPolygon in input:
			try:
				# Define the id for a given poly
				ID = int(aPolygon['properties']['id'])
				# Define coords and convert back to a poly item
				Geom = aPolygon['geometry']['coordinates'][0]
				Geom = tuple(Geom)
				from shapely.geometry import Polygon
				Po = Polygon(Geom)
				# Write an insert item consisting of id and poly coords
				InsertItem = [ID, Po]
			except:
				print 'Error with record attribute: %i' % i
				errorRec.append(i)
				pass
			try:
				if Po.is_valid==True:
					TempDF = pd.DataFrame(InsertItem)
					# Rotate the data to match our desired format
					TempDF = TempDF.transpose()
					# Insert the column names
					TempDF.columns = ['id', 'geometry']
					ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)
			except:
				print 'Error with record True/False Handle: %i' % i
				errorRec.append(i)
				pass

		# Convert the dataframe to a geodataframe
		gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
		# Loop through remainder of files to compare the previously opened one
		# to the rest of them.
		for shpfl in range(len(ParsedShapes)):
			with fiona.open(ParsedShapes[shpfl]) as put:
				# Second dataframe for the current shapefile
				ShapeFileDF2 = pd.DataFrame(columns=['id', 'geometry'])
				# Extract the polygons from the file
				for aPolygon in put:
					try:
						# Define the id for a given poly
						ID = int(aPolygon['properties']['id'])
						# Define coords and convert back to a poly item
						Geom = aPolygon['geometry']['coordinates'][0]
						Geom = tuple(Geom)
						from shapely.geometry import Polygon
						Po = Polygon(Geom)
						# Write an insert item consisting of id and poly coords
						InsertItem = [ID, Po]
					except:
						print 'Error with record attribute: %i' % i
						errorRec.append(i)
						pass
					try:
						if Po.is_valid==True:
							TempDF = pd.DataFrame(InsertItem)
							# Rotate the data to match our desired format
							TempDF = TempDF.transpose()
							# Insert the column names
							TempDF.columns = ['id', 'geometry']
							ShapeFileDF2 = ShapeFileDF2.append(TempDF, ignore_index = True)
					except:
						print 'Error with record True/False Handle: %i' % i
						errorRec.append(i)
						pass
			gdf2 = gpd.GeoDataFrame(ShapeFileDF2, geometry='geometry')
			# # ['id_left' 'geometry' 'index_right' 'id_right']
			# Combine the files by spatial join
			combine = gpd.sjoin(gdf, gdf2, how="left", op='intersects')
			# Remove pairs that are null, meaning it was matched with itself
			combine = combine[combine['id_left']!=combine['id_right']]
			# Drop any nan values
			combine = combine.dropna()
			# Drop the geometry and index, we only need the relationship data
			combine = combine.drop(columns=['geometry', 'index_right'])
			MasterDF = MasterDF.append(combine, ignore_index = True)
	MasterDF.to_csv(ParseCSV_Dir+str(i)+'MetaRelate.csv')
	MasterDF = pd.DataFrame(columns=['id_left', 'id_right'])

