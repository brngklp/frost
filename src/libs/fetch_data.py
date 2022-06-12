from libs.get_index import site_index
import json

def fetch_data(filename: str, target: str) -> str: 
    """
    Read the file by website and return the username and password of the given site.
    """
    index_file = site_index(filename, target)
    def read_file(filename: str) -> dict:
        """
        Read from json file and fetch the usernames and passwords
        """
        with open(filename, "r") as f:
            data = json.load(f)
        # Assign the username and password to variables and return them  
        username = data[index_file]["username"]
        password = data[index_file]["password"]
        return f"{username}, {password}"
    return read_file(filename)

#print(fetch_data("/home/dank/.frost/store/dank.json", "https://github.com"))