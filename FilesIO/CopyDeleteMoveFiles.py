import os
import shutil

initial_path = os.path.abspath('.')
initial_path = os.path.join(initial_path, 'sample_files')
print(initial_path)


################################
# Copy files
################################
file_a = os.path.join(initial_path, 'a.txt')
file_c = os.path.join(initial_path, 'c.txt')

shutil.copy(file_a, file_c)

################################
# Move files
################################

file_d = os.path.join(initial_path, 'd.txt')
shutil.move(file_c, file_d)

################################
# Delete files (move to recycling bin)
################################

import send2trash

send2trash.send2trash(file_d)


