import Modules
from Modules import *

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


# Shapefile = 'C:/Users/WindowShop/Documents/GitHub/Landsat-DEM-Processing/567Contour.shp'

# Write a shapefile with buffers

# ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
# with fiona.open(Shapefile) as input:
# 	print '\nAdding Buffers...\n'
# 	ProgBarLimit = len(input)
# 	for i in tqdm.tqdm(range(ProgBarLimit)):
# 		Polygon = input[i]
# 		# Define the id for a given poly
# 		ID = int(Polygon['properties']['id'])
# 		Geom = Polygon['geometry']['coordinates'][0]
# 		Geom = tuple(Geom)
# 		from shapely.geometry import Polygon
# 		Po = Polygon(Geom)
# 		BFP = Po.buffer(0.1)
# 		InsertItem = [ID, BFP]
# 		TempDF = pd.DataFrame(InsertItem)
# 		# Rotate the data to match our desired format
# 		TempDF = TempDF.transpose()
# 		# Insert the column names
# 		TempDF.columns = ['id', 'geometry']
# 		ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)

# # Convert the dataframe to a geodataframe
# gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# # No refrence system is in this file yet, we must set it to the correct one
# # before changing it.
# gdf.crs = fiona.crs.from_epsg(26914)
# # Write a shapefile from the geodataframe object
# print 'Writting the shapefile...'
# gdf.to_file("567WithBuff_.1.shp")

########################################################################


Shapefile = 'C:/Users/WindowShop/Documents/GitHub/Landsat-DEM-Processing/567WithBuff_.1.shp'

# with fiona.open(Shapefile) as input:
# 	for 

# from shapely.ops import cascaded_union
# polygons = gpd.read_file(Shapefile)
# boundary = gpd.GeoSeries(cascaded_union(polygons))
# boundary.plot(color = 'red')
# plt.show()

# from shapely.geometry import Point, LineString, shape, mapping
# from shapely.ops import cascaded_union
# import fiona
# import shapely
# from shapely.ops import unary_union, polygonize
# from osgeo import ogr
# from shapely.strtree import STRtree

# with fiona.open(Shapefile) as layer:
# 	# ProgBarLimit = len(layer)
# 	ProgBarLimit = 100
# 	for i in tqdm.tqdm(range(ProgBarLimit)):
# 		Temp=[]
# 		ID = []
# 		# for n,pol in enumerate(subset):
# 		if type(shape(layer[i]['geometry'])) == shapely.geometry.polygon.Polygon:
# 			Temp.append(shape(layer[i]['geometry']))
# 			ID.append(layer[i]['id'])

# rings = [LineString(list(pol.exterior.coords)) for pol in Temp]
# union = unary_union(rings)
# print rings
# print len(Temp)
# sys.exit()

# tree = STRtree(Temp)
# result = [geom for geom in polygonize(union)]

# final=[]

# for k,item in enumerate(result):
# 	print(len(result),k)
# 	touch=tree.query(item.centroid)
# 	inside=[]
# for x in touch:
# 	if x.contains(item.centroid):
# 		inside.append(item)
# 	if len(inside)>=1:
# 		final.append(item)


# print final

#########################################################################

# ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])

# from shapely.geometry import Polygon
# from shapely.strtree import STRtree

# temp = []
# limit = 10
# i = 0
# results = []
# with fiona.open(Shapefile) as layer:
# 	ProgBarLimit = len(layer)
# 	# ProgBarLimit = limit
# 	print 'Extracting polygons...'
# 	for i in tqdm.tqdm(range(ProgBarLimit)):
# 		x = layer[i]['geometry']['coordinates'][0]
# 		x = tuple(x)
# 		x = Polygon(x)
# 		temp.append(x)
# 	s = STRtree(temp)
# 	print STRtree[0]
# 	sys.exit()

# 	# ProgBarLimit = len(layer)
# 	ProgBarLimit = limit
# 	print 'Searching of polygon intersections...'
# 	for i in tqdm.tqdm(range(ProgBarLimit)):
# 		x = layer[i]['geometry']['coordinates'][0]
# 		x = tuple(x)
# 		x = Polygon(x)
# 		query_geom = x
# 		result = s.query(query_geom)
# 		results.append(layer[i]['id'])

# df = pd.DataFrame(results)
# df.columns = ['ID']
# print 'Writting csv...'
# df.to_csv('intersectionMeta.csv')


#######################################################################



# 	p = 0
# 	for polygon in layer:
# 		if polygon['id']==results[p]:
# 			Geom = tuple(polygon['geometry']['coordinates'][0])
# 			Po = Polygon(Geom)
# 			ID = polygon['id']
# 			# Write an insert item from the id, elevation, and geometry of the polygon
# 			InsertItem = [ID, Po]
# 			TempDF = pd.DataFrame(InsertItem)
# 			# Rotate the data to match our desired format
# 			TempDF = TempDF.transpose()
# 			# Insert the column names
# 			TempDF.columns = ['id', 'geometry']
# 			ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)




# # Convert the dataframe to a geodataframe
# gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# # No refrence system is in this file yet, we must set it to the correct one
# # before changing it.
# gdf.crs = fiona.crs.from_epsg(26914)
# # Write a shapefile from the geodataframe object
# print 'Writting the shapefile...'
# gdf.to_file("TESTOVERLAP.shp")
# # print len(results)
# # print results
###########################################################################
# import itertools
# p = []
# i = 0
# with fiona.open(Shapefile) as layer:
# 	for polygon in layer:
# 		p.append(polygon['geometry'])
# 		i+1
# 		if i==10:
# 			break
# 			print 'break'
# geoms = p.tolist()
# print geoms
# intersection_iter = gpd.GeoDataFrame(gpd.GeoSeries([poly[0].intersection(poly[1]) for poly in  itertools.combinations(geoms, 2) if poly[0].intersects(poly[1])]), columns=['geometry'])
# union_iter = intersection_iter.unary_union
# union_iter.to_file("intersection_iter.shp") 
###############################################################################

# USE*** This will parse the larger file by thousands for easier iteration


# ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
# counter = 0
# errorRec = []
# FinalI = 0
# with fiona.open(Shapefile) as input:
# 	print '\nParsing the shapefile...\n'
# 	ProgBarLimit = len(input)
# 	# ProgBarLimit = 3000
# 	for i in tqdm.tqdm(range(ProgBarLimit)):
# 		try:
# 			Polygon = input[i]
# 			# Define the id for a given poly
# 			ID = int(Polygon['properties']['id'])
# 			Geom = Polygon['geometry']['coordinates'][0]
# 			Geom = tuple(Geom)
# 			from shapely.geometry import Polygon
# 			Po = Polygon(Geom)
# 			InsertItem = [ID, Po]
# 		except:
# 			print 'Error with record attribute: %i' % i
# 			errorRec.append(i)
# 			pass
# 		try:
# 			if Po.is_valid==True:
# 				TempDF = pd.DataFrame(InsertItem)
# 				# Rotate the data to match our desired format
# 				TempDF = TempDF.transpose()
# 				# Insert the column names
# 				TempDF.columns = ['id', 'geometry']
# 				ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)
# 				counter = counter+1
# 				FinalI = i
# 		except:
# 			print 'Error with record True/False Handle: %i' % i
# 			errorRec.append(i)
# 			pass

# 		if counter==1000:
# 			# Convert the dataframe to a geodataframe
# 			gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# 			gdf.crs = fiona.crs.from_epsg(26914)
# 			FileName = str(i+1)+'Iteration.shp'
# 			gdf.to_file(Parse_Dir+FileName)
# 			ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
# 			counter=0

# if len(ShapeFileDF)!=0:
# 	# Convert the dataframe to a geodataframe
# 	gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# 	gdf.crs = fiona.crs.from_epsg(26914)
# 	FileName = str(FinalI+1)+'Iteration.shp'
# 	gdf.to_file(Parse_Dir+FileName)

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
			# Write a list item
			# CL = combine.values.tolist()
			# Relations.append(CL)
			# print combine
			MasterDF = MasterDF.append(combine, ignore_index = True)

print MasterDF

