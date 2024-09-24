# the os module

import os

def find(path, dir):
    found_paths = []
    directories = os.listdir(path)
    for d in directories:
        full_path = os.path.join(path, d)
        if os.path.isdir(full_path):
            if d == dir:
                found_paths.append(full_path)
            else:
                find(full_path, dir) # Recurse into the subdirectory
    
    for p in found_paths:
        print(p)

find(path="/Users/esteban/Downloads", dir="basb")