import shelve
import os

initial_path = os.path.abspath('.')
print(initial_path)
file_path = os.path.join(initial_path, 'sample_files')


# Serialize and save into key-based file data store
shelve_file = os.path.join(file_path, 'shelve-dump.p')
integers = [1, 2, 3, 4, 5]

with shelve.open(shelve_file, 'c') as shelf:
    shelf['ints'] = integers


# Reading from the data store

with shelve.open(shelve_file, 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]))
