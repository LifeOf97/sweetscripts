# Author: Kelvin Mayowa Ayeni (KMA).
# Github: d-kma.
# Twitter: @DBlackerMan.
# Date: February 19, 2021.
# formula: https://www.techspot.com/news/68482-quickly-convert-between-storage-size-units-kb-mb.html
# Credits: https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size

import argparse

# initialize the argparse module
parser = argparse.ArgumentParser()
# create an optional argument to parse value to this program
parser.add_argument("-s", "--size", type=int, help="Enter the value to convert to human readable size")
args = parser.parse_args() # get all args here


def humanize(value: any, decimal: int=2, memory: float=1000.0, spc: bool=False) -> str:
    """
    function to convert values in digits to human readable sizes

    value:
    the value to convert, this should be type int or float.

    decimal:
    The number of decimal places the converted size should be returned in.
    default is 2 decimal place.

    memory:
    default memory size to use. Gigabyte: 1000.0 or Gibibyte: 1024.0.
    default is Gigabyte: 1000.0 look up "formula" url @ top comments.

    spc:
    should there be spacing between the converted size and its unit
    when outputting the converted size?. True/False.
    default is False: no spacing.
    """
    # we set value to "any" because users can provide either int or float,
    # iterate over the units the amount of times it takes for the value
    # to be divided by the memory size until the new value is less then
    # the memory size then append that current unit value as its suffix.
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']:
        # if the value is less than the memory size "1024.0"
        if abs(value) < memory:
            if spc: # if the user wants spacing between size and unit.
                return F"{value:.{decimal}f} {unit}"
            else:
                return F"{value:.{decimal}f}{unit}"
        # if the value is still not less than the memory size, divide again.
        value /= memory


# this function is called when these script is called from th command line
# without any command-line argument passed along side.
def prompt():
    value: int = int(input("Enter a size to convert: "))

    # while the value is not to close this program.
    while value not in ['end', 'close', 'cls', 'exit', 'x']:
        print(f"Size: {humanize(value)}")
        break


if __name__ == "__main__":
    if args.size: # if command-line arg is passed with one of [-s, --size]
        print(f"Size: {humanize(args.size)}")
    else:
        prompt()
else:
    prompt()