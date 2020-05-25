file = open('demo3.txt', 'w')
result = [1,2,3,4,5]

file.writelines(str(result))
# [file.write(str(x)) for x in result]

# import os
# os.mkdir('files')
# os.rmdir('files')
# print(os.listdir('files'))