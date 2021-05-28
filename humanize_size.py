# Author: Kelvin Mayowa Ayeni (KMA).
# Github: d-kma.
# Twitter: @DBlackerMan.
# Date: February 19, 2021.
# formula: https://www.techspot.com/news/68482-quickly-convert-between-storage-size-units-kb-mb.html
# Credits: https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size

import argparse
import typing

# initialize the argparse module
parser = argparse.ArgumentParser()
# create an optional argument to parse value to this program
parser.add_argument("-s", "--size", type=int, help="Enter the value to convert to human readable size")
args = parser.parse_args() # get all args here


def humanize(value: typing.Union[int, float], decimal: int=2, memory: float=1024.0, spc: bool=False) -> str:
    """
    function to return human readable sizes

    value:
    the value to convert, this should be either int or float.

    decimal:
    The number of decimal places the converted size should be returned in.
    default is 2 decimal place.

    memory:
    default memory size to use. kilobyte: 1024.0.

    spc:
    should there be spacing between the converted size and its unit
    when outputting the converted like - '12 MB/12MB'. True/False.
    default is False: no spacing.
    """
    # for every division that occures, iterate over the units until the
    # value is less than the memory size, then append that current unit
    # to the value as its suffix :).
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']:
        # check if the value inputed is less than the memory size "1024.0"
        if abs(value) < memory:
            if spc: # if the user wants spacing between size and unit.
                return F"{value:.{decimal}f} {unit}"
            else:
                return F"{value:.{decimal}f}{unit}"
        # if the value is not less than the memory size, divide the value
        # by the memory size.
        value /= memory


# this function is executed when these script is called
# from the command line without any command-line argument
# passed along side.
def prompt():

    # check input type
    try:
        value = input("Enter memory size or ['x' to exit] : ") 
        
        if '.' in value: # convert to type float
            value = float(value)
        else:
            value = int(value) # convert to type int

    except ValueError: # if its really a string, check
        if value in ['exit', 'x']:
            print("Exitted.")
        else:
            prompt()

    except KeyboardInterrupt:
        print("\nExitted.")
    
    else:
        print(f"Memory size is : {humanize(value)}")


if __name__ == "__main__":
    if args.size: # if command-line arg is passed with one of [-s, --size]
        print(f"Memory size is : {humanize(args.size)}")
    else:
        prompt()
else:
    prompt()