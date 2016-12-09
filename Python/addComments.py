#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import sys
import fileinput

if len(sys.argv) >= 2:
        root = str(sys.argv[1])
else:
        sys.exit()
py_files = list()
if os.path.exists(root):
        for root, dirs, files in os.walk(root):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
else:
        sys.exit()

def addComments(file):
        count = 0
        line_count = 0
        for line in fileinput.input(file, inplace=True):
            if line[:2] != '#!':
                if line_count == 0:
                    print "#!/usr/bin/env python\n",
                    line_count = line_count + 1
                if count == 0:
                    print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n#\t\tFile Owner - Kartheek Palepu\t\t#\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"+line,
                    count = count + 1
                else:
                    print line,
            else:
                print line,
                line_count = line_count + 1

py_files = [addComments(i) for i in py_files]
