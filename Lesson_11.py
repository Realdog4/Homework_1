import os

directory_file = os.getcwd()


def write_directory(directory):
    filenames = os.listdir(directory)
    dir_names = []
    dir_files = []
    for file in filenames:
        fullpath = os.path.join(directory, file)
        if os.path.isdir(fullpath):
            dir_names.append(file)
        elif os.path.isfile(fullpath):
            dir_files.append(file)
    dict_directories = {'filenames': dir_files, 'dirnames': dir_names}
    return dict_directories


directories = write_directory(directory_file)
directories_copy = write_directory(directory_file)
print(directories)

bool_value = True


def dict_sorted(directory, b_value):
    swap = not b_value
    list_names = []
    x = list(directory.keys())

    for list_item in directory.values():
        list_item.sort(key=str.lower, reverse=swap)
        list_names.append(list_item)

    directories_sorted = {x: list_names.pop(0) for x in x}

    return directories_sorted


sorted_file = dict_sorted(directories, bool_value)
print(sorted_file)

user_string = "flat.txt"


def directory_append(dicter, string):
    if string.__contains__("."):
        value = list(dicter.values())[0]
        value.append(string)
        dicter.update({'filenames': value})
    else:
        value = list(dicter.values())[1]
        value.append(string)
        dicter.update({'dirnames': value})

    return dicter


directory_update = directory_append(directories_copy, user_string)
print(directory_update)
