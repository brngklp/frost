#!?
# This library is created for project frost as it's logger.
# Licensed under the GPL3 General Public License
# Archived: 11/28/21-2:15_PM

import os
import logging
from datetime import datetime
from dataclasses import dataclass, asdict
from getpass import getuser
from pathlib import Path

@dataclass
class LogData:
    # This strftime below is for disabling the milisecond.
    time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    username: str = getuser()
    success: bool = False

    def __repr__(self) -> str:
        return f"[{self.time}]: User {self.username} tried a password, The password was {self.success}"

@dataclass
class FileHandling:
    location: str = f"/home/{LogData.username}/.passwded-store/logs/main.log"
    createFolderLocation: str = f"/home/{LogData.username}/.passwded-store/logs"

def writeLogToFile(*args,**kwargs) -> None:
    # First check if the directory exists. If not, then create it.
    checkdir = os.path.exists(FileHandling.createFolderLocation)
    # Check if there is a directory already exists. And if not so, create it
    if checkdir == False:
        Path(FileHandling.createFolderLocation).mkdir(parents=True, exist_ok=False)
    
    #raise SystemExit("There is already a directory at the location. Refusing to create it.")
    # Then with using logging library, write the logs to a file.
    logging.basicConfig(
        filename=f"{FileHandling.location}",
        filemode='w',
        format='%(message)s'
    )
    # Check if the password user tried was true or not

