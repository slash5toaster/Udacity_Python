import os
# 1. Get filenames
# 2. for each filename
#    2.1 calculate updated filename
#    2.2 rename file to updated filename
#    2.3

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("/Users/jonesc47/Google Drive/Python/PythonClass_Udacity/Secret_Message/prank"):
    f.extend(filenames)
    break
# print(f.filenames)
