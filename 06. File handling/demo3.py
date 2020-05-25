from os import listdir
from os.path import join, isdir, isfile, walk

def print_directory_tree(folder_path, on_file_found):
    contents_path = [join(folder_path, content) for content in listdir(folder_path)]
    [on_file_found(file) for file in contents_path if isfile(file)]
    [print_directory_tree(dir, on_file_found) for dir in contents_path if isdir(dir)]

def file_contains_text(file_path,text):
    file = open(file_path, 'r')
    line = file.readline()

    while line:
        if text in line:
            return True
        return False

def print_file_if_containing_text(file_path):
    text = 'random'
    if file_contains_text(file_path, text):
        print(file_path)
folder_path = 'files'
print_directory_tree(folder_path, print_file_if_containing_text)


