#Delete the Empty Folder

import os
import os.path

os.rmdir('Folder1')
a = os.listdir('.')
print(a)