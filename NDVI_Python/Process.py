
# Imports for program
import Imports
from Imports import *

# Write directories for final output files
dir = 'Output'
if not os.path.exists(dir):
    os.makedirs(dir)

dir = 'Output/CLIP_IMAGE'
if not os.path.exists(dir):
    os.makedirs(dir)

# Define folder paths
SF_Dir = 'Shapefile/'
PLD = 'ParsedLakeData/'

###############################################################################
# Define an object containing the path row information for the whole data set

# Open txt file to extract path and row information
DocObj = []
with open('PATH_ROW.txt') as doc:
	for aItem in doc:
		DocObj.append(aItem)

# Clean up the data for use
# Split list
DocObj = DocObj[0].split(']')
# Remove final item from each set and create list of path row variables
PR = []
for aItem in DocObj:
	# Pass the blank object left over from the split
	if aItem != '':
		aItem = aItem.replace('[', '')
		aItem = aItem.split('/')
		PR.append(aItem)

# Write index to determine how many segments are present, as well as IDs
ID = []
i=0
with fiona.open(SF_Dir+'LakeSeg.shp') as LK:
	for feature in LK:
		ID.append(i)
		i=i+1

SegCount = 0
ProgBarLimit = len(ID)
# ProgBarLimit = 3
NDVI_IMAGE_PATHS = []

print '\nBuilding Segment NDVI...\n'
for r in tqdm.tqdm(range(ProgBarLimit)):
	SHPfl = 'Segment%i/%iSegShp/%iSegShp.shp' % (SegCount, SegCount, SegCount)
	GenFileOutLoc = 'Segment%i/' % (SegCount)
	SHPflFolder = 'Segment%i/%iSegShp/' % (SegCount, SegCount)
	# Loop through the lake segments and write data

	############################################################################
	#						Path Row Discovery Section
	
	# Determine which path/row the polygon should be related to

	wrs = gpd.GeoDataFrame.from_file(SF_Dir+'WRS2_descending.shp')

	file1 = gpd.read_file(PLD+SHPfl)
	# Select correct path and row for given polygon. This will ensure the 
	# correct .tif image is used for the calculation
	CorrectPR = []

	#Reproject file1 to wrs' crs, assuming it's available
	file1 = file1.to_crs(wrs.crs)

	wrs_intersection = wrs[wrs.intersects(file1.geometry[0])]

	paths, rows = wrs_intersection['PATH'].values, wrs_intersection['ROW'].values
	# print paths
	# sys.exit()
	# Write list for max and min x y for paths
	MxMn = []

	# Iterate through each Polygon of paths and rows intersecting the area
	for i, row in wrs_intersection.iterrows():
	    # Convert row to polygon, geometry attribut contains all
	    # coordinates
	    poly = Polygon(row.geometry)
	    # Append max and min to list
	    MxMn.append(poly.bounds)

	# identify max and min xy for the target shapefile. This will be used to determine if 
	# multiple images are required.

	SelectionMXMN = file1.bounds

	# If only one path/row combo, opt to use them as the correct one
	if len(MxMn)==1:
		Row = rows.tolist()
		Path = paths.tolist()
		CorrectPR=[str(Path[0]), str(Row[0])]

	# Identify which scenes are needed. If multiple are
	# selected, filter through to check which is best fit.

	if len(MxMn)>1:
		# In list, Max x is most negative; Min x is least negative;
		# Max y is greatest number, Min y is second largest. (Logic valid for 
		# North America)

		# Convert bounds of Rivermile to list for order
		# temp = file3.bounds
		temp = file1.bounds
		List = temp.values.tolist()

		# Format (Max x, Min x, Min y, Max y)
		ListRMSort = sorted(List[0])

		# Loop through scenes to see which one fully encompasses area.
		# Also select which image is most centered on RM.

		# Differences calculates the difference between max and min 
		# coordinates between the scene and Rivermile selection
		Differences = []
		temp = []

		for aItem in MxMn:
			# Order coordinates from least to greatest 
			Order = sorted(aItem)
			i = 0
			# Loop calculation for each scene
			for var in Order:
				# Calculate the difference between variables
				# ListRMSort is the iteration of max and min
				# for the Rivermile selection.
				x = var-ListRMSort[i]
				i = i+1
				temp.append(x)
			Differences.append(temp)
			temp = []
		# Relationship between Differences and shape:
		# Valid if x for each var is => ( - , + , - , + )
		# If multiple scenes are valid, the one containing largest
		# valid difference is selected as it is most centered.

		Valid = []
		# 1 is no
		# 2 is yes
		temp = []
		for aList in Differences:
			i = 0
			temp = []
			for aItem in aList:
				# Identify if each variable for [0] and [2] are correct
				if i == 0 or i == 2:
					if aItem > 0:
						temp.append(1)
					if aItem < 0:
						temp.append(2)
				# Identify if each variable for [1] and [3] are correct
				if i == 1 or i == 3:
					if aItem < 0:
						temp.append(1)
					if aItem > 0:
						temp.append(2)
				i = i+1

			# Determine which scenes are valid
			# Use counter to determine keys (which numbers are present)
			y = collections.Counter(temp)
			Variables = y.keys()
			# If length is 1, all values are either correct or incorrect
			if len(Variables)==1:
				for aItem in Variables:
					if aItem == 1:
						Valid.append(1)
					if aItem == 2:
						Valid.append(2)
			# If lenght is greater than 1, then not all are true. 
			# Therefore, the set is not sufficient for the whole
			# study area.
			if len(Variables) > 1:
				Valid.append(1)
			temp = []

		# If value in Valid are 1, the scene does not fully cover the area.
		# If value in Valid is 2, the scene covers the study area entirely.

		# Select which scene covers area. If both fail, then both will be used.
		# This is because it takes 2 images to cover the area.
		i = 0
		SelectScene = []
		for aItem in Valid:
			if aItem==2:
				SelectScene.append(i)
			if aItem!=2:
				pass
			i = i+1

		# If multiple pass, select which is most centered.
		# Differences between Max and Min values to Rivermile
		Mx = []
		My = []
		Mnx = []
		Mny = []
		i = 0
		temp = []
		# Which scene has highest distance for that variable
		HighestDist = []

		if len(SelectScene) > 1:
			# Add separate variables for diff to
			# individual list for ordering
			for aList in Differences: 
				Mx.append(aList[0])
				Mnx.append(aList[1])
				Mny.append(aList[2])
				My.append(aList[3])
			# Sort the lists in order
			# Most negative is furthest
			Mx = sorted(Mx)
			# Higher positive is further
			Mny = sorted(Mny)
			# Most negative is furthest
			Mnx = sorted(Mnx)
			# Higher positive is further
			My = sorted(My)

			for aList in Differences: 
				# Highest Diff Max x
				if aList[0]==Mx[0]:
					temp.append(i)
				if aList[0]!=Mx[0]:
					temp.append('Null')
				# Highest Diff Min x
				if aList[1]==Mnx[0]:
					temp.append(i)
				if aList[1]!=Mnx[0]:
					temp.append('Null')
				# Highest Diff Min y
				if aList[2]==Mny[-1]:
					temp.append(i)
				if aList[2]!=Mny[-1]:
					temp.append('Null')
				# Highest Diff Min y
				if aList[3]==My[-1]:
					temp.append(i)
				if aList[3]!=My[-1]:
					temp.append('Null')
				HighestDist.append(temp)
				temp = []
				i = i+1
			# Min and Max y can be the same. This is the Latitude of image.
			# Check if a set completely satisfies coverage or if multiple 
			# images are required.
			i = 0
			Reject = []
			for aList in HighestDist:
				for aItem in aList:
					if aItem=='Null':
						Reject.append(i)
				i = i+1
			# Count which are rejected based on index
			SceneR = collections.Counter(Reject)
			RejectedScenes = SceneR.keys()

			# Check if all scenes rejected
			DownloadAll = []
			if len(RejectedScenes)==len(wrs_intersection):
				DownloadAll.append(2)

			# Index and count all scenes for selection of best 
			i = 0
			Index = []

			for aItem in range(len(wrs_intersection)):
				Index.append(i)
				i=i+1

			res = list(set(Index)-set(RejectedScenes))
			Index = 0
			if len(res)==1:
				for i, row in wrs_intersection.iterrows():
					if Index==res[0]:
						# Create a string for the name containing the path and row of this Polygon
						name = 'path: %03d, row: %03d' % (row.PATH, row.ROW)
						CorrectPR = [str(row.PATH), str(row.ROW)]
					if Index!=res[0]:
						pass
					Index = Index + 1

	#						Path Row Discovery Section END
	############################################################################
	
	#							Calculate Segement NDVI

	# Convert the CorrectPR to an image code similar to the 
	# image file name/directory.
	ConvertT = []
	for aItem in CorrectPR:
		if aItem>3:
			# If only 2 numbers are present, a 0 needs to be placed in front of the
			# variable.
			InsertItem = '0'+aItem
			ConvertT.append(InsertItem)
	CPR = ConvertT[0]+ConvertT[1]
	


	# Identify folder paths within image output
	LANDSAT_PATH = glob('TIF_Code_Images*/*')

	# List of folders containing files
	Paths = []
	# Files within each folder
	Files = []

	for aItem in LANDSAT_PATH:
		# Select the path and row for the image collection to 
		# compare to the CorrectPR object
		S = aItem.split('\\')
		SCode = str(S[-1])
		# Use the satellite code to write an output folder for the ndvi calc
		NDVIOUT = SCode+'_'+'NDVI'
		SCode = SCode.split('_')
		# Satellite
		SAT = SCode[0]
		# Date
		Date = SCode[-1]
		# Path and Row
		PR = SCode[1]
		# Compare the PR code to the CorrectPR
		# If the item matches, then the image file
		# for that PR will be selected for the NDVI analysis
		if PR==CPR:
			Paths.append(aItem)
			L = listdir(aItem)
			Files.append(L)

	# Define NDVI output folder specific to image being used
	# NDVIOUT = 
	dir = 'ParsedLakeData/Segment%i/Seg%iNDVI/%s' % (SegCount, SegCount, NDVIOUT)
	if not os.path.exists(dir):
		os.makedirs(dir)
	NDVIoutMain = 'ParsedLakeData/Segment%i/Seg%iNDVI/%s/' % (SegCount, SegCount, NDVIOUT)

	# Select the B3 and B4 bands
	# Define the imagery for the path and row of the polygon
	# print Paths
	for aItem in glob(Paths[0]+'*/*B4.TIF'):
		OriginalData = aItem
		B4 = aItem
	for aItem in glob(Paths[0]+'*/*B3.TIF'):
		B3 = aItem
		Temp = aItem
		crop_extent = gpd.read_file(PLD+SHPfl)
		Temp = rasterio.open(Temp)
		crop_extent = crop_extent.to_crs(Temp.crs)
		Save = crop_extent.to_file(PLD+SHPflFolder+str(SegCount)+'Extent'+'.shp')
		# To show the extent of shapefile

		# Plot extent
		# fig, ax = plt.subplots(figsize=(6, 6))
		# crop_extent.plot(ax=ax)
		# ax.set_title("Shapefile Crop Extent",
		#              fontsize=16)
		# # plt.show()
		# plt.close()

	import rasterio.mask
	with fiona.open(PLD+SHPflFolder+str(SegCount)+'Extent'+'.shp', "r") as shapefile:
		shapes = [feature["geometry"] for feature in shapefile]

	with rasterio.open(B4) as src:
		out_image_B4, out_transform4 = rasterio.mask.mask(src, shapes, crop=True)
		out_meta_B4 = src.meta
		# Define the parameters of the tif clip
		out_meta_B4.update({"driver": "GTiff",
                 "height": out_image_B4.shape[1],
                 "width": out_image_B4.shape[2],
                 "transform": out_transform4})
	# Write a clipped b4 tif file
	with rasterio.open(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B4Clip.tif', 'w', **out_meta_B4) as dst:
	    dst.write(out_image_B4)
		# print out_meta_B4
		# print out_transform4
	with rasterio.open(B3) as src:
		out_image_B3, out_transform = rasterio.mask.mask(src, shapes, crop=True)
		out_meta_B3 = src.meta
		# Define the parameters of the tif clip
		out_meta_B3.update({"driver": "GTiff",
                 "height": out_image_B3.shape[1],
                 "width": out_image_B3.shape[2],
                 "transform": out_transform4})
	# Write a clipped b4 tif file
	with rasterio.open(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B3Clip.tif', 'w', **out_meta_B4) as dst:
	    dst.write(out_image_B3)
		# show(out_image_B3)

	# Open the clipped bands for the NDVI calculation
	# We write the new tif files and open them for the calculation to aid in 
	# writing a new tif file for the ndvi calculation. Error was lifted when 
	# trying to save the ndvi tif image from the clips of band imagery.
	with rasterio.open(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B4Clip.tif') as src:
		out_image_B4, out_transform4 = rasterio.mask.mask(src, shapes, crop=True)
		out_meta_B4 = src.meta
	with rasterio.open(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B3Clip.tif') as src:
		out_image_B3, out_transform3 = rasterio.mask.mask(src, shapes, crop=True)
		out_meta_B3 = src.meta

	# Calculate NDVI
	# Allow division by zero
	np.seterr(divide='ignore', invalid='ignore')
	ndvi_upper = (out_image_B4.astype(float) - out_image_B3.astype(float))
	ndvi_lower = (out_image_B4.astype(float) + out_image_B3.astype(float))
	ndvi = (ndvi_upper / ndvi_lower)

	# Update the meta data the new 
	out_meta_B4.update({"driver": "GTiff",
	                 "height": out_image_B4.shape[1],
	                 "width": out_image_B4.shape[2],
	                 "transform": out_transform4,
	                 # Define dytpe as float to accomodate for the dec in calc
	                 "dtype": "float64"})

	# Write the calculated NDVI data to a tif image
	with rasterio.open(NDVIoutMain+'seg'+str(SegCount)+'-'+str(Date)+'ndvi.tif', 'w', **out_meta_B4) as dst:
	    dst.write(ndvi)

	# Delete the band clips previously written
	os.remove(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B4Clip.tif')
	os.remove(PLD+GenFileOutLoc+'seg'+str(SegCount)+'B3Clip.tif')

	# Write a png output folder for figures
	dir = 'ParsedLakeData/Segment%i/Seg%iNDVI_PNG' % (SegCount, SegCount)
	if not os.path.exists(dir):
		os.makedirs(dir)
	NDVIfigures = 'ParsedLakeData/Segment%i/Seg%iNDVI_PNG/' % (SegCount, SegCount)


	# Plot NDVI data
	fig, ax = plt.subplots(figsize=(12,6))
	# print ndvi[0]
	data2 = np.rollaxis(ndvi[0], 0, 1)

	data3 = ax.imshow(data2, cmap='plasma', vmin=-1, vmax=1)
	fig.colorbar(data3, fraction=.05)
	ax.set(title='NDVI Segment %i' % SegCount)
	ax.set_axis_off()
	Input = SAT + '\n' + PR + '\n' + Date
	plt.text(1,1, Input)
	# plt.show()
	plt.savefig(NDVIfigures+'seg'+str(SegCount)+'_'+str(Date)+'ndvi.png')
	plt.close()
	NDVI_IMAGE_PATHS.append(NDVIoutMain+'seg'+str(SegCount)+'-'+str(Date)+'ndvi.tif')
	SegCount = SegCount+1
	# sys.exit()

	#						Calculate Segment NDVI END

###################################################################################
						# Merge NDVI tif Files

print NDVI_IMAGE_PATHS

src_files_to_mosaic = []
for fp in NDVI_IMAGE_PATHS:
	src = rasterio.open(fp)
	src_files_to_mosaic.append(src)

mosaic, out_trans = merge(src_files_to_mosaic)

show(mosaic, cmap='terrain')

