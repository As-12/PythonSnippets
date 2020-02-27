import os


# Get current directory in absolute path
initial_path = os.path.abspath('.')
print(initial_path)

# join directory
new_path = os.path.join(initial_path, 'sample_files')

# Check if dir is valid
if os.path.isdir(new_path):
    print(f'{new_path} is a valid directory')

# Open and read a file
file_a = os.path.join(new_path, 'a.txt')

with open(file_a, 'r') as f:
    count = 0
    for line in f.readlines():
        print(f'{count}: {line}')
        count += 1


# Write to a textfile.

file_b = os.path.join(new_path, 'b.txt')

fileOut = open(file_b, 'w')

with open(file_a, 'r') as fileIn:
    with open(file_b, 'w') as fileOut:
        count = 0
        for line in fileIn.readlines():
            fileOut.write(f'{count}: {line}')
            count += 1




