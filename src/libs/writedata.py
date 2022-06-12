# TODO: write data's into a json file
import json
import os
from getpass import getuser
from typing import Optional
from dataclasses import dataclass, field
from libs.create import createFile
from libs.id import generate_id
from libs.encrypt import sym_encrypt
@dataclass
class WriteInfo:
    homeUser: str = getuser()
    fileLocation: str = field(init=False, repr=False)    

    def __post_init__(self):
        self.fileLocation = f"/home/{self.homeUser}/.frost/store/{self.homeUser}.json"

def updateDatabase(site: str, username: str, password: str, mail: Optional[str]) -> None:
    """
    This function was created for writing all the data to the database.
    """
    filename: str = WriteInfo().fileLocation

    if os.path.exists(filename):
        pass
    else:
        createFile(filename)

    listObj = []
    with open(filename) as f:
        listObj = json.load(f)
    password = sym_encrypt(password)

    jsonDict = { 
        "id": generate_id(username),
        "username": f"{username}",
        "mail": f"{mail}",
        "site": f"{site}",
        "password": f"{password}",
    }
    
    listObj.append(jsonDict)

    with open(filename, 'w') as fp:
        json.dump(listObj, fp, indent=4)

# Example: updateDatabase("https://github.com", "barannnnn", "baran123", "baran@gmail.com")