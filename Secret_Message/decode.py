import os
import string
from os import listdir
from os.path import isfile, join

#Our plan
# 1. Get filenames
# 2. for each filename
#    2.1 calculate updated filename
#    2.2 rename file to updated filename

mypath = "/Users/jonesc47/Google Drive/Python/PythonClass_Udacity/Secret_Message/prank"

#get all the files in the directory
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# act on each file
for fle in onlyfiles:
    print fle
    for nums in range(9):
        fle = string.replace(fle, str(nums),'',3)
    print "-- " + fle

## End of the File, If this is missing File has been truncated
