import Modules
from Modules import *

# import SubMod
# from SubMod import *

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


# Shapefile = '567Contour.shp'

# # Write a shapefile with buffers

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
# print 'Writting the shapefile: 567WithBuff_.1.shp'
# gdf.to_file("567WithBuff_.1.shp")

# ########################################################################


# Shapefile = '567WithBuff_.1.shp'


# # USE*** This will parse the larger file by thousands for easier iteration


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

#######################################################################

# Relate each subset of data to other subsets, then write a csv document to 
# save memory for the device.

# Open parsed dataset piece by piece for comparison

# Write list of shapefiles in directory

# ParsedShapes = []
# for file in os.listdir(Parse_Dir):
#     if file.endswith(".shp"):
#         ParsedShapes.append(Parse_Dir+file)

# MasterDF = pd.DataFrame(columns=['id_left', 'id_right'])
# ProgBarLimit = len(ParsedShapes)
# for i in tqdm.tqdm(range(ProgBarLimit)):
# 	ShapeFileDF = pd.DataFrame(columns=['id', 'geometry'])
# 	# Open file to be compaired with
# 	with fiona.open(ParsedShapes[i]) as input:
# 		# Extract the polygons from the file
# 		for aPolygon in input:
# 			try:
# 				# Define the id for a given poly
# 				ID = int(aPolygon['properties']['id'])
# 				# Define coords and convert back to a poly item
# 				Geom = aPolygon['geometry']['coordinates'][0]
# 				Geom = tuple(Geom)
# 				from shapely.geometry import Polygon
# 				Po = Polygon(Geom)
# 				# Write an insert item consisting of id and poly coords
# 				InsertItem = [ID, Po]
# 			except:
# 				print 'Error with record attribute: %i' % i
# 				errorRec.append(i)
# 				pass
# 			try:
# 				if Po.is_valid==True:
# 					TempDF = pd.DataFrame(InsertItem)
# 					# Rotate the data to match our desired format
# 					TempDF = TempDF.transpose()
# 					# Insert the column names
# 					TempDF.columns = ['id', 'geometry']
# 					ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)
# 			except:
# 				print 'Error with record True/False Handle: %i' % i
# 				errorRec.append(i)
# 				pass

# 		# Convert the dataframe to a geodataframe
# 		gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# 		# Loop through remainder of files to compare the previously opened one
# 		# to the rest of them.
# 		for shpfl in range(len(ParsedShapes)):
# 			with fiona.open(ParsedShapes[shpfl]) as put:
# 				# Second dataframe for the current shapefile
# 				ShapeFileDF2 = pd.DataFrame(columns=['id', 'geometry'])
# 				# Extract the polygons from the file
# 				for aPolygon in put:
# 					try:
# 						# Define the id for a given poly
# 						ID = int(aPolygon['properties']['id'])
# 						# Define coords and convert back to a poly item
# 						Geom = aPolygon['geometry']['coordinates'][0]
# 						Geom = tuple(Geom)
# 						from shapely.geometry import Polygon
# 						Po = Polygon(Geom)
# 						# Write an insert item consisting of id and poly coords
# 						InsertItem = [ID, Po]
# 					except:
# 						print 'Error with record attribute: %i' % i
# 						errorRec.append(i)
# 						pass
# 					try:
# 						if Po.is_valid==True:
# 							TempDF = pd.DataFrame(InsertItem)
# 							# Rotate the data to match our desired format
# 							TempDF = TempDF.transpose()
# 							# Insert the column names
# 							TempDF.columns = ['id', 'geometry']
# 							ShapeFileDF2 = ShapeFileDF2.append(TempDF, ignore_index = True)
# 					except:
# 						print 'Error with record True/False Handle: %i' % i
# 						errorRec.append(i)
# 						pass
# 			gdf2 = gpd.GeoDataFrame(ShapeFileDF2, geometry='geometry')
# 			# # ['id_left' 'geometry' 'index_right' 'id_right']
# 			# Combine the files by spatial join
# 			combine = gpd.sjoin(gdf, gdf2, how="left", op='intersects')
# 			# Remove pairs that are null, meaning it was matched with itself
# 			combine = combine[combine['id_left']!=combine['id_right']]
# 			# Drop any nan values
# 			combine = combine.dropna()
# 			# Drop the geometry and index, we only need the relationship data
# 			combine = combine.drop(columns=['geometry', 'index_right'])
# 			MasterDF = MasterDF.append(combine, ignore_index = True)
# 	MasterDF.to_csv(ParseCSV_Dir+str(i)+'MetaRelate.csv')
# 	MasterDF = pd.DataFrame(columns=['id_left', 'id_right'])

######################################################################################

# open csv data to check for relations between variables
# Memory error when all data opened at once
# Write list of csv files

CSVFILES = []
for file in os.listdir(ParseCSV_Dir):
    if file.endswith(".csv"):
        CSVFILES.append(ParseCSV_Dir+file)

# Write all csv data to single list
# AllData = []
# for csv in CSVFILES:
# 	with open(csv) as csvfile:
# 		for aItem in csvfile:
# 			# Clean up the data
# 			aItem = str(aItem)
# 			aItem = aItem.replace('\n', '')
# 			aItem = aItem.split(',')
# 			# Filter out headers from the csv files
# 			# Append the now pristien, clean information to a list
# 			if aItem!=['', 'id_left', 'id_right']:
# 				AllData.append(aItem[-2::])

# ProgBarLimit = len(AllData)
# # A list containing called items
# CalledItems = []

# TheMatches = []
# for i in tqdm.tqdm(range(ProgBarLimit)):
# 	Set = AllData[i]
# 	Relate = [Set[0], Set[1]]
# 	count = 0
# 	if i ==0:
# 		# If the loop has not yet completed its first round, we will have no
# 		# previously called items. So we will start the list here.
# 		CalledItems.append(Set[0])
# 		CalledItems.append(Set[1])
# 	if i!=0:
# 		# Lets go ahead and remove doubles of values from the called dataset
# 		CalledItems = CalledItems.keys()

# 		# If i is not 0 then the loop has completed once or multiple times, we will
# 		# check the list of called items to see if one of the variables being pulled
# 		# from the root of this loop for comparison has already been related. If so,
# 		# we will return and pick a different root set for comparison.
# 		for Variable in Relate:
# 			for previouslycalled in CalledItems:
# 				if Variable==previouslycalled:
# 					print 'HA! Gotcha!'
# 					sys.exit()
# 	while count < len(AllData):
# 		# Call each set in alldata
# 		for aSet in AllData:
# 			# Call an individual value in alldata set
# 			for aItem in aSet:
# 				# Append to CalledItems, we will do a key collection later to
# 				# remove the doubles.
# 				CalledItems.append(aItem)
# 				# Call the items in our relation
# 				for RItem in Relate:
# 					# If an item from the set in alldata is the same as a single
# 					# object in our relate list, then the set is related
# 					if aItem==RItem:
# 						# Now call the set object we need to relate
# 						if aItem!=aSet[0]:
# 							Relate.append(aItem)
# 						if aItem!=aSet[1]:
# 							Relate.append(aItem)
# 			Relate = Relate.keys()
# 		# Count the set from alldata just processed
# 		count = count+1
# 	TheMatches.append(Relate)





########################################################################################
# AllData = []
# for csv in CSVFILES:
# 	with open(csv) as csvfile:
# 		for aItem in csvfile:
# 			# Clean up the data
# 			aItem = str(aItem)
# 			aItem = aItem.replace('\n', '')
# 			aItem = aItem.split(',')
# 			# Filter out headers from the csv files
# 			# Append the now pristien, clean information to a list
# 			if aItem!=['', 'id_left', 'id_right']:
# 				AllData.append(aItem[-2::])

ProgBarLimit = len(CSVFILES)
# A list containing called items
CalledItems = []

TheMatches = []
AllData = []
SI = 0
for i in tqdm.tqdm(range(ProgBarLimit)):
	with open(CSVFILES[i]) as csvfile:
		AllData=[]
		for aItem in csvfile:
			# Clean up the data
			aItem = str(aItem)
			aItem = aItem.replace('\n', '')
			aItem = aItem.split(',')
			# Filter out headers from the csv files
			# Append the now pristien, clean information to a list
			if aItem!=['', 'id_left', 'id_right']:
				AllData.append(aItem[-2::])
	# Start the data analysis
		Set = AllData[SI]
		Relate = [Set[0], Set[1]]
		if SI ==0:
			# If the loop has not yet completed its first round, we will have no
			# previously called items. So we will start the list here.
			CalledItems.append(Set[0])
			CalledItems.append(Set[1])
		if SI!=0:
			# Lets go ahead and remove doubles of values from the called dataset
			CalledItems = CalledItems.keys()

			# If i is not 0 then the loop has completed once or multiple times, we will
			# check the list of called items to see if one of the variables being pulled
			# from the root of this loop for comparison has already been related. If so,
			# we will return and pick a different root set for comparison.
			for Variable in Relate:
				for previouslycalled in CalledItems:
					if Variable==previouslycalled:
						print 'HA! Gotcha!'
						sys.exit()
		count = 0
		while count < len(AllData):
			# Call each set in alldata
			for aSet in AllData:
				# print aSet
				# Call an individual value in alldata set
				for aItem in aSet:
					# print aItem
					# if count==100:
					# 	sys.exit()
					# sys.exit()
					# Append to CalledItems, we will do a key collection later to
					# remove the doubles.
					CalledItems.append(aItem)
					# Call the items in our relation
					for RItem in Relate:
						# If an item from the set in alldata is the same as a single
						# object in our relate list, then the set is related
						if aItem==RItem:
							# print aItem
							# print RItem
							# sys.exit()
							# Now call the set object we need to relate
							if aItem==aSet[0]:
								# print aSet
								Relate.append(aItem)
								# print Relate
							if aItem==aSet[1]:
								Relate.append(aItem)
							# sys.exit()
							# print len(Relate)
							Relate = collections.Counter(Relate)
							Relate = Relate.keys()
			# Count the set from alldata just processed
			count = count+1
		TheMatches.append(Relate)
		sys.exit()
		SI = SI+1