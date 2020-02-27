import zipfile
import os

initial_path = os.path.abspath('.')
print(initial_path)

# join directory
path = os.path.join(initial_path, 'sample_files')
##########################
# Compressing files
##########################
with zipfile.ZipFile(os.path.join(path, 'compressed.zip'), 'w') as zipObj:
   # Add multiple files to the zip
   zipObj.write(os.path.join(path, 'a.txt'))
   zipObj.write(os.path.join(path, 'b.txt'))







