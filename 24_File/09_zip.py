import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('example.txt', arcname='example.txt')  # arcname to avoid full path in zip
    zipf.write('example_copy.txt', arcname='example_copy.txt')

    file_to_zip = ['data.json', 'example.txt']
    for file in file_to_zip:
        zipf.write(file, arcname=file)