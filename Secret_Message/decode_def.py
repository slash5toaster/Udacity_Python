import os
import string
from os import listdir
from os.path import isfile, join

#Our plan
# 1. Get filenames
# 2. for each filename
#    2.1 calculate updated filename
#    2.2 rename file to updated filename
def rename_file()


# mypath = "/Users/jonesc47/Google Drive/Python/PythonClass_Udacity/Secret_Message/prank"
# assumes the
mypath = os.getcwd() + "/prank"

#get all the files in the directory
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
print
# act on each file
for fle in onlyfiles:
    print fle,

    #save the decoded file name
    decoded_fle = fle

    os.rename(join(mypath,fle),join(mypath,decoded_fle))

## End of the File, If this is missing File has been truncated
