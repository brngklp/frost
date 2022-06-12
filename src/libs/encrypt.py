from cryptography.fernet import Fernet
import libs.readkey

def sym_encrypt(password: str) -> bytes:
    # Take the password from the argv and turn the string password into a bytes object
    password = password.encode()
    # Take the key from the function readkey()
    key = libs.readkey.readkey() 
    # Encrypt the password with the key using fernet.
    f = Fernet(key)
    password = f.encrypt(password)
    # Now the password is encrypted, so we can save the password at the next function
    return password
