try:
    file_path = 'files\\text.txt'
    file = open(file_path, 'r')
    for line in file:
        print(line, end='')
    print('File found')
except:
    print('File not found')
finally:
    file.close()