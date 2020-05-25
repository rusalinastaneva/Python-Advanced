try:
    file_path = 'demo2.py'
    file = open(file_path, 'w')
except FileNotFoundError:
    print("File not found or path is incorrect")
finally:
    print("exit")
