import Modules
from Modules import *

# Write an object containing all folders with DEM poly data
# Append a system path
sys.path.append("Output/DEM_Poly")
Poly_Dir = 'Output/DEM_Poly/'

# Write list of all folders (Shapefile names will be based off folder names)
Folders = os.listdir(Poly_Dir)

# Write a data frame for all polygons to be placed into
ShapeFileDF = pd.DataFrame(columns=['id', 'elevation', 'geometry'])

ProgBarLimit = len(Folders)

# Extract all the polygons at a specified elevation level
print '\nExtracting DEM Polygons...\n'
for i in tqdm.tqdm(range(ProgBarLimit)):
	# Define shapefile name from folder name
	SF = 'dem'+Folders[i]+'.shp'
	# Define the item for opening as the folder path and the shapefile name
	Shapefile = Poly_Dir+Folders[i]+'/'+SF
	# Open the shapefile as input
	with fiona.open(Shapefile) as input:
		# Filter through each item in input, in this case its a polygon
		for Polygon in input:
			# Define the elevation as a callable item
			Elevation = Polygon['properties']['elev']
			# Filter said elevation
			if Elevation==567:
				ID = Polygon['id']
				Geom = Polygon['geometry']['coordinates'][0]
				# In order to remake a polygon, we must import Polygon again here.
				# Then the list of coordinates is converted to a tuple object
				# instead of a list. From there you can convert the tuple to a poly.
				from shapely.geometry import Polygon
				Geom = tuple(Geom)
				Po = Polygon(Geom)
				# Write an insert item from the id, elevation, and geometry of the polygon
				InsertItem = [ID, Elevation, Po]
				TempDF = pd.DataFrame(InsertItem)
				# Rotate the data to match our desired format
				TempDF = TempDF.transpose()
				# Insert the column names
				TempDF.columns = ['id', 'elevation', 'geometry']
				ShapeFileDF = ShapeFileDF.append(TempDF, ignore_index = True)

# Convert the dataframe to a geodataframe
gdf = gpd.GeoDataFrame(ShapeFileDF, geometry='geometry')
# No refrence system is in this file yet, we must set it to the correct one
# before changing it.
gdf.crs = fiona.crs.from_epsg(26914)
# Write a shapefile from the geodataframe object
print 'Writting the shapefile...'
gdf.to_file("567Contour.shp")
