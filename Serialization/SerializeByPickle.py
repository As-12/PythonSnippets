import pickle
import os

initial_path = os.path.abspath('.')
print(initial_path)
file_path = os.path.join(initial_path, 'sample_files')


# Saving object using pickle
integers = [1, 2, 3, 4, 5]

save_file = os.path.join(file_path, 'pickle-dump.p')
with open(save_file, 'wb') as pfile:
    pickle.dump(integers, pfile)

# Reading object using pickle

with open(save_file, 'rb') as pfile:
    result = pickle.load(pfile)
    print(result)


