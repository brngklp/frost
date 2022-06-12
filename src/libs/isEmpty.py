import os
def isEmpty(filename) -> bool:
    check = os.stat(filename).st_size
    if check == 0:
        return True
    else:
        return False
