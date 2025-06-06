#Delete all the files with folder which contains in the folder

import os
import os.path
import shutil  

shutil.rmtree('TestingFolder')
a= os.listdir('.')
print(a)