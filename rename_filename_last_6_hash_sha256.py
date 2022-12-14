import os, re, random, string, shutil
import hashlib

PATH = r"F:/test"
FILES = []
PATTERN = "\\b[^\d\W]+\\b"

def hash_file(file):
    with open(file, 'rb') as f:
        content = f.read()
        hashes = hashlib.sha256(content).hexdigest()
        return(hashes[-6:])

def clean(file_path):
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path).lower()
    fname, ext = os.path.splitext(base_name)
    
    r = re.findall(PATTERN, fname)
    if r:
        fname = " ".join(r)
    else:
        fname = str(random.randint(1111,9999))
    
    base_name = fname + " " + hash_file(file_path) + ext
    new_file_path = os.path.join(dir_name, base_name)
    return new_file_path

for root, dirs, files in os.walk(PATH):
    for file in files:
        file_loc = os.path.join(root, file)
        new_file_loc = clean(file_loc)
        os.rename(file_loc, new_file_loc)
        print(file)
