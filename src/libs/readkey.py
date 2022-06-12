from dataclasses import dataclass, field
from getpass import getuser


@dataclass
class Read:
    homeuser: str = getuser()
    fileLocation: str = field(init=False, repr=False)

    def __post_init__(self):
        self.writeFile = f'/home/{self.homeuser}/.frost/store/frost.json'
        self.folderLocation = f'/home/{self.homeuser}/.frost/keys'
        self.fileLocation = f'/home/{self.homeuser}/.frost/keys/{self.homeuser}.key'

def readkey() -> bytes:
    # Read the key file's data
    with open(Read().fileLocation, 'rb') as f:
        data = f.read()
    # And then return the data
    return data
