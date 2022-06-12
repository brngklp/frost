import os
from libs.defaultFile import defaultFile
from libs.isEmpty import isEmpty

def createFile(filename):
    if os.path.isfile(filename) is False:
        defaultFile(filename)            
    else:
        if isEmpty(filename):
            defaultFile(filename)
        else:
            exit(f"ERR: Refusing to overwrite an existing file. File Location: {filename}")