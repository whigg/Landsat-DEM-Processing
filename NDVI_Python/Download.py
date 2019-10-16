# Imports for program
import Imports
from Imports import *

PATH = 33
ROW = 27

# Write output folder for download
dir = 'Data'
if not os.path.exists(dir):
    os.makedirs(dir)

dir = 'Data/CSV'
if not os.path.exists(dir):
    os.makedirs(dir)

dir = 'Data/RAW_IMAGE'
if not os.path.exists(dir):
    os.makedirs(dir)

dir = 'Data/IMAGE'
if not os.path.exists(dir):
    os.makedirs(dir)

destdir = 'Data/CSV/'

sys.path.append('Data/RAW_IMAGE/')
#***********************************************************************

# Find all available data for given Row and Path

if not os.path.exists(destdir+str(PATH)+'_'+str(ROW)+'.csv'):
	print'nope'
	sys.exit()
	chunk_container = pandas.read_csv('Data/CSV/index.csv', sep=',', chunksize=5000)

	check = 0
	Data = []

	for chunk in chunk_container:
		chunk = chunk.drop(columns=['PRODUCT_ID', 'SPACECRAFT_ID', 
			'SENSOR_ID','COLLECTION_NUMBER', 'SENSING_TIME',
			'NORTH_LAT', 'SOUTH_LAT', 'WEST_LON', 'EAST_LON', 
			'TOTAL_SIZE', 'BASE_URL', 'DATA_TYPE'])
		# Dataframe Format: ['SCENE_ID', 'DATE_ACQUIRED', 
		#'COLLECTION_CATEGORY', 'WRS_PATH', 'WRS_ROW', 'CLOUD_COVER']

		#Define Selection
		df = chunk[(chunk.WRS_PATH == 33)&(chunk.WRS_ROW == 27)]

		if len(df)>0:
			temp = df.values.tolist()
			for aItem in temp:
				Data.append(aItem)

	df = pd.DataFrame(Data, columns = ['SCENE_ID', 'DATE_ACQUIRED','COLLECTION_CATEGORY', 'WRS_PATH', 'WRS_ROW', 'CLOUD_COVER'])

	df.to_csv(destdir+str(PATH)+'_'+str(ROW)+'.csv')

#**********************************************************************

# Define start and end dates

year_start =int(2018)
month_start=int(06)
day_start  =int(01)
date_start =datetime.datetime(year_start, month_start, day_start)

year_end =int(2018)
month_end=int(8)
day_end  =int(15)
date_end =datetime.datetime(year_end, month_end, day_end)

# Open data csv to filter which satellite images are needed for analysis
#			Columns:
# ['SCENE_ID', 'DATE_ACQUIRED','COLLECTION_CATEGORY', 
# 'WRS_PATH', 'WRS_ROW', 'CLOUD_COVER']

# Open csv
df = pandas.read_csv(destdir+str(PATH)+'_'+str(ROW)+'.csv')
# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Convert date to datetime
df['DATE_ACQUIRED'] = pd.to_datetime(df['DATE_ACQUIRED'])  

# Select images between start and end date
mask = (df['DATE_ACQUIRED'] > date_start) & (df['DATE_ACQUIRED'] <= date_end)
# Use mask to define new date selection
dfSelect = df.loc[mask]


# Drop landsat 8 (LC8 is landsat 8)
temp = dfSelect.values.tolist()
temp2 = []
for aItem in temp:
	if aItem[0][0:3] != 'LC8':
		temp2.append(aItem)

# Write new dataframe with correct dates and satellite
dfSelect = pd.DataFrame(temp2, columns = ['SCENE_ID', 'DATE_ACQUIRED','COLLECTION_CATEGORY', 'WRS_PATH', 'WRS_ROW', 'CLOUD_COVER'])
print dfSelect
sys.exit()
# Select lowest cloud coverage
CloudMax = 5.0
mask = (dfSelect['CLOUD_COVER'] < CloudMax)
dfSelect = dfSelect.loc[mask]

# Write list of images to download
temp = dfSelect.values.tolist()

# List only SCENE_ID for download
Scenes = []
for aItem in temp:
	Scenes.append(aItem[0])


#**********************************************************

# Download Data

# Initialize a new API instance and get an access key
username = 'EnviBio'
password = 'Marine613'

print '%i Scene(s) Preparing to Download...' % len(Scenes)
ee = EarthExplorer(username, password)

ProgBarLimit = len(Scenes)
i = 0

print ('Initiating Download...')
for aItem in Scenes:
	ee.download(scene_id=aItem, output_dir='Data/RAW_IMAGE')
	i = i+1
ee.logout()

#************************************************************
# Unzip files
temp = list(os.listdir('Data/RAW_IMAGE'))
Loc = 'Data/RAW_IMAGE/'

i = 0
for aItem in temp:
	fname = Loc+aItem
	# Write folder for specific images
	dir = 'Data/IMAGE/'+Scenes[i]
	if not os.path.exists(dir):
	    os.makedirs(dir)
	# Find and extract all files 
	if (fname.endswith(".tar.gz")):
		tar = tarfile.open(fname, "r:gz")
		tar.extractall(path=dir)
		tar.close()
	elif (fname.endswith("tar")):
		tar = tarfile.open(fname, "r:")
		tar.extractall(path=dir)
		tar.close()
	i = i+1
#************************************************************