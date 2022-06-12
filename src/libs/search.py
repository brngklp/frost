# Created for the project frost by Baran Gokalp
# Date: 21/01/2022-16:49PM

class DataNotFound(Exception):
    """
    This is a custom exception class for when the target is not found in the dataset
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

def search(dataset: list[str], website: str) -> int:
    """
    This function takes a sorted dataset and a target then It return's the location of target.
    We'll be using linear search algorithm agonizingly.
    """
    # I actually wanted to use a "n log n" sorting algorithm and binary search as 
    # the search algorithm but I was literally stuck for a long time.
    # If you have any idea how to do it, please let me know in the issues section or if you have a working piece of code
    # please submit a pull request at github.
    if website not in dataset:
        # If target is not in the dataset, return an error
        raise DataNotFound(f"Target {website} not found in dataset")
    else:
        for i in range(len(dataset)):
            if dataset[i] == website:
                return i
        
# usage: search(["abc.xyz", "google.com"], "abc.xyz")