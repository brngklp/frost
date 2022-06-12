# DONE
from functools import reduce

def generate_id(username: str) -> int:
    # Multiplication function for capital pi function
    def times(x,y) -> int: 
        return x*y
    """
    Sigma Function below takes the length of the string and 
    returns the sum from 1 to character length. 
    More details on Maths_Behind.pdf file.
    """
    sigma = lambda username: sum([i for i in range(0, len(username) + 1)])
    #!FIXME: sigma function reproduces weird results. Instead of returning the result of x, it returns x+1
    #!FIXED: sigma function now returns the correct result.
    product = lambda username: reduce(times, range(1, len(username) + 1))
    
    """
    Product Function Takes the length of the string and 
    returns the product from 1 to character length. 
    More details on Maths_Behind.pdf file.
    """
    length = len(username)
    if length > 8:
        process = sigma(username)
    else:
        process = product(username)
    
    return process
