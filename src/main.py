# Libraries of Frost
import libs.clipboard
import libs.fetch_data
import libs.log
import libs.writedata
import libs.genkey
import libs.credentials
import libs.id
import libs.genpass
import libs.create
import libs.encrypt
import libs.search
import libs.defaultFile
import libs.get_index
import libs.readkey
import libs.isEmpty
import libs.timeout
import libs.genpass
# Other Libraries required
import argparse 
import sys

def main() -> None:
    """
    Usage manual for frost.
    After all the installations are done, do the following:
    $ frost init
    this will create your keyfiles and store them in your home directory.
    """
    # Description of the program.
    parser = argparse.ArgumentParser(description='Frost is a password manager', epilog="Thanks for using Frost")
    # Program name
    parser.prog = 'frost'
    # Available arguments
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("-i", "--init", action='store_true' ,required=False, help="Initialize Frost")
    parser.add_argument("-s", "--store", required=False, help="Print out the websites", type=str)
    parser.add_argument("-c", "--clipboard", required=False, help="Copy the password to the clipboard", type=str)
    parser.add_argument("-a", "--add", nargs='?', help="Add a new website", type=str)
    # If no argument provided, print out the help message
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)    
    # Parse the arguments
    args = parser.parse_args()
    # If the given argument is init
    if args.init is not False:
        # Create the keyfiles
        libs.genkey.genkey()
    # If the given argument is store
    if args.store is not False:
        # Fetch the data from the file
        libs.fetch_data.fetch_data(args.store)   
    libs.writedata.updateDatabase("asdas", "baran92", "baran123", "baran@gmail.com") 
if __name__ == """__main__""":
    main()
