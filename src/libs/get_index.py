import libs.readjson
import libs.credentials

class DataNotFound(Exception):
    """
    This is a custom exception class for when the target is not found in the dataset
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

def site_index(filename: str, target: str) -> str:
    """
    Return the index of the target website in the dataset
    """
    dataset = libs.readjson.read_file(filename)
    website = libs.credentials.addHttp(target)
    # Check If the dataset contains the website 
    if website in dataset:
        # If contains, then return the index of the website
        return dataset.index(website)
    else:
        raise DataNotFound(f"Target {website} not found in dataset")

#filename = "/home/dank/.frost/store/dank.json"
#print(process(filename, "https://github.com"))