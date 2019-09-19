######################################################################
# This is the master file for the program! From here it will collect #
# and process the data. (Basic implementation currently)             #
######################################################################
import Modules
from Modules import *

print 'Please select Module/s to run:\n1) LiDar Download\n2) LiDar to Polygon Processing\n3) Extract Contour (Currently 567)\n4) All of the above'

query = raw_input('What module would you like to run?:')

query = int(query)

if query==1:
	import DownloadLidar

if query==2:
	import DEMPOLY
if query==3:
	import Extract567

if query==4:
	import DownloadLidar
	import DEMPOLY
	import Extract567











