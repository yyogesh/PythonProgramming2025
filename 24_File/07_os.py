import os
import shutil


if os.path.exists('example.txt'):
    print('example.txt exists')
    print('File size:', os.path.getsize('example.txt'), 'bytes')
else:
    print('example.txt does not exist')

shutil.copy2('example.txt', 'example_copy.txt')