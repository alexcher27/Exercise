import os  , sys
from fnmatch import fnmatch
path = sys.argv[1]
pattern = "*.sh"


def read_first_line(file_path):
    with open(file_path) as f:
        first_line = f.readline().rstrip()

    return first_line

def get_folder_items(folder_path, file_pattern):
    file_list = []
    for folder_path, subdirs, files in os.walk(folder_path):
        for name in files:
            if fnmatch(name, file_pattern):
                file_list.append(os.path.join(folder_path, name))

    return file_list





files = get_folder_items(path, pattern)
namespaces = {}

for f in files:
    namespace = read_first_line(f)
    if namespace.startswith("#!"):
        if namespace in namespaces:
            namespaces[namespace] += 1
        else:
            namespaces[namespace] = 1

for k, v in namespaces.items():
    print(str(v) + ' ' + k)



