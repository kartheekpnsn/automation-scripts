import os
from fnmatch import fnmatch

root = "PROJECT_PATH/src"

pattern = "*.py"

def get_files(files, pattern = "*.py"):
	return [os.path.join(path, name) for name in files if fnmatch(name, pattern)]

python_files = []
for path, subdirs, files in os.walk(root):
    python_files.extend(get_files(files))

def is_import(line):
	flag = False
	if 'from ' in line:
		if 'import ' in line:
			flag = True
	elif 'import ' in line:
		flag = True
	return flag

def get_imports(file):
	with open(file, 'r') as fObj:
		lines = fObj.read().splitlines()
	return [line.strip() for line in lines if is_import(line)]

all_imports = []
for file in python_files:
	all_imports.extend(get_imports(file))

with open("all_imports.txt", "w") as fObj:
	fObj.write("\n".join(list(set(all_imports))))
