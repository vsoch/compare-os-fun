import platform
import pickle
import sys
import re
import os

# This small script will print the list of folders for a file system to a text file, 
# intended to run on a node to compare file systems across nodes

output_folder = sys.argv[1]
node = platform.node()
regexp = '^/tmp|^/home|^/scratch|^/scratch-local|^/share/PI'
output_file = "%s/%s.txt" %(output_folder,node)
dirs = []

if not os.path.exists(output_file):
    for root, directories, filenames in os.walk('/'):
        if not re.search(regexp,root):
            for directory in directories:
                dirname = os.path.join(root,directory)
                dirs.append(dirname)
    pickle.dump(dirs,open(output_file,'wb'))
