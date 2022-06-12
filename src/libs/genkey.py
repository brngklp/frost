from dataclasses import dataclass, field
from getpass import getuser
from pathlib import Path
from cryptography.fernet import Fernet
import os

@dataclass
class Symmetric:
    homeuser: str = getuser()
    writeFile: str = field(init=False, repr=False)
    fileLocation: str = field(init=False, repr=False)
    folderLocation: str = field(init=False, repr=False) 

    def __post_init__(self):
        self.writeFile = f'/home/{self.homeuser}/.frost/store/frost.json'
        self.folderLocation = f'/home/{self.homeuser}/.frost/keys'
        self.fileLocation = f'/home/{self.homeuser}/.frost/keys/key.key'

def genkey() -> None:
    # Check if the location exists
    fileLoc = Path(Symmetric().fileLocation)
    folderLoc = Path(Symmetric().folderLocation)
    # First create the folder
    folderLoc.mkdir(parents=True, exist_ok=True)
    # Create a url safe base64 encoded key
    key = Fernet.generate_key()
    # Let's make this function more secure :)
    # First check if the file exists
    if fileLoc.is_file():
        # If the file exists, then check if it's empty or not
        isEmpty = os.stat(fileLoc).st_size == 0
        # If the file is empty, then proceed to write the key.
        if isEmpty == True:
            with open(fileLoc, 'wb') as f:
                f.write(key)
        elif isEmpty == False:
            exit("There is a file exists in the keyfile's location. Please remove it to proceed.")
    else:
        with open(fileLoc, 'wb') as f:
            f.write(key)