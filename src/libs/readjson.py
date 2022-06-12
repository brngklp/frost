import json

def read_file(filename: str) -> list[str]:
    """
    Read from json file and fetch the websites. Then append the websites to a list and return it.
    """
    with open(filename, "r") as f:
        # Fetch the keyword named site
        data = json.load(f)
        websites = []
        # Append the elements to the list
        for x in data:
            website = x["site"]
            websites.append(website) 
        return websites
