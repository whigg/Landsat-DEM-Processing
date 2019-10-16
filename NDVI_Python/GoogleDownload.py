import Imports
from Imports import *

# Season date logic. This section will allow for an indepth download of seasonal
# data for iteration. In order to select seasons, start/mid/end image dates must
# be defined. This will allow for a chronological assessment, as well as additional
# error checks for cloud coverage.

# Month range for season start range
SeasonST1 = '5-15'
SeasonST2 = '6-15'
# Mid season range
SeasonM1 = '6-15'
SeasonM2 = '8-1'
# End season range
SeasonE1 = '8-1'
SeasonE2 = '8-31'

SL = [[SeasonST1, SeasonST2], [SeasonM1, SeasonM2], [SeasonE1, SeasonE2]]

# Year range for the assessment
Years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
    '2009', '2010', '2011','2012', '2014', '2015', '2016', '2017', '2018', '2019']

########################################################################
     # Multiple scene download
# # Define the download process for the loop
# def filteredImageInCHIRPSToMapId(dateFrom, dateTo, Path, Row):
#     if year < 2013:
#         eeCollection = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR")
#     if year > 2013:
#         eeCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
#     # geometry = ee.Geometry.Point([47.52,-101.78])
#     # colorPalette='ffffff,307b00,5a9700,86b400,b4cf00,e4f100,ffef00,ffc900,ffa200,ff7f00,ff5500'
#     # visParams={'opacity':1,'max':188.79177856445312,'palette':colorPalette}
#     eeFilterDate = ee.Filter.date(dateFrom, dateTo)
#     eeCollection = eeCollection.filter(ee.Filter.eq('WRS_PATH', Path))
#     eeCollection = eeCollection.filter(ee.Filter.eq('WRS_ROW', Row))
#     eeCollection = eeCollection.filter(ee.Filter.lt('CLOUD_COVER', 15))
#     eeCollection = eeCollection.filter(eeFilterDate)

#     Info = eeCollection.getInfo()


#     # Info = eeCollection.getInfo()['features'][0]['properties']
#     FirstIm = [str(Info['features'][0]['id'])]
#     FirstIm = ee.Image(FirstIm).select(['B3'])

#     SecondIm = [str(Info['features'][0]['id'])]
#     SecondIm = ee.Image(SecondIm).select(['B4'])

#     # Format a file name using landsat image name. This will help
#     # filter image by date and P/R when pulling from Google Drive.

#     Name = str(Info['features'][0]['id'])
#     Split = Name.split('/')
#     BaseFileName = Split[-1]

#     out = batch.Export.image(FirstIm, description=BaseFileName+'_B3')
#         # region=ee.Feature(FirstIm.first()).geometry().bounds().getInfo()['coordinates'])
#     ## Process the image
#     process = batch.Task.start(out)

#     process
#     out = batch.Export.image(SecondIm, description=BaseFileName+'_B4')
#         # region=ee.Feature(FirstIm.first()).geometry().bounds().getInfo()['coordinates'])
#     ## Process the image
#     process = batch.Task.start(out)

#     process


# # Start the download process (This sends the data to google drive)
# ee.Initialize()
# # Open txt file to determine path and row information
# PR = []
# with open('PATH_ROW.txt') as doc:
#     for aItem in doc:
#         PR.append(aItem)

# # Clean up the data

# # Split Returns: ['[34/27', '[32/27', '[33/27', '']
# PR = PR[0].split(']')
# # Remove blank spot
# PR.remove('')
# # Now remove the [
# PR_Filtered = []
# for aItem in PR:
#     aItem = aItem.replace('[', '')
#     aItem = aItem.split('/')
#     PR_Filtered.append(aItem)
    
# print PR_Filtered

# ProgBarLimit = len(PR_Filtered)

# print '\nDownloading Image Bands...\n'
# for i in tqdm.tqdm(range(ProgBarLimit)):
#     Path = int(PR_Filtered[i][0])
#     Row = int(PR_Filtered[i][1])
#     filteredImageInCHIRPSToMapId('2011-06-01', '2011-07-15', Path, Row)

####################################################################################

# Download single scene at different dates

# Define the download process for the loop
def filteredImageInCHIRPSToMapId(dateFrom, dateTo, Path, Row, Y):
    Y = int(Y)
    if Y < 2013:
        eeCollection = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR")
        Band1 = 'B3'
        Band2 = 'B4'
    if Y > 2013:
        Band1 = 'B4'
        Band2 = 'B5'
        eeCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
    # geometry = ee.Geometry.Point([47.52,-101.78])
    # colorPalette='ffffff,307b00,5a9700,86b400,b4cf00,e4f100,ffef00,ffc900,ffa200,ff7f00,ff5500'
    # visParams={'opacity':1,'max':188.79177856445312,'palette':colorPalette}
    eeFilterDate = ee.Filter.date(dateFrom, dateTo)
    eeCollection = eeCollection.filter(ee.Filter.eq('WRS_PATH', 34))
    eeCollection = eeCollection.filter(ee.Filter.eq('WRS_ROW', 27))
    eeCollection = eeCollection.filter(ee.Filter.lt('CLOUD_COVER', 15))
    eeCollection = eeCollection.filter(eeFilterDate)

    Info = eeCollection.getInfo()

    # Info = eeCollection.getInfo()['features'][0]['properties']
    FirstIm = [str(Info['features'][0]['id'])]
    FirstIm = ee.Image(FirstIm).select([Band1])

    SecondIm = [str(Info['features'][0]['id'])]
    SecondIm = ee.Image(SecondIm).select([Band2])

    # Format a file name using landsat image name. This will help
    # filter image by date and P/R when pulling from Google Drive.

    Name = str(Info['features'][0]['id'])
    Split = Name.split('/')
    BaseFileName = Split[-1]

    out = batch.Export.image(FirstIm, description=BaseFileName+'_'+Band1)
        # region=ee.Feature(FirstIm.first()).geometry().bounds().getInfo()['coordinates'])
    ## Process the image
    process = batch.Task.start(out)

    process
    out = batch.Export.image(SecondIm, description=BaseFileName+'_'+Band2)
        # region=ee.Feature(FirstIm.first()).geometry().bounds().getInfo()['coordinates'])
    ## Process the image
    process = batch.Task.start(out)

    process


ProgBarLimit1 = len(Years)
ProgBarLimit2 = len(SL)

ee.Initialize()

ErrorLog = []

print '\nDownloading Image Bands...\n'
for i in tqdm.tqdm(range(ProgBarLimit1)):
    Path = 34
    Row = 27
    Y = Years[i]
    for t in tqdm.tqdm(range(ProgBarLimit2)):
        Sep = SL[t]
        dateFrom = str(Y+'-'+Sep[0])
        dateTo = str(Y+'-'+Sep[1])
        try:
            filteredImageInCHIRPSToMapId(dateFrom, dateTo, Path, Row, Y)
        except Exception as e:
            Item = [Sep, dateFrom, dateTo, e]
            ErrorLog.append(Item)
            pass

print ErrorLog


