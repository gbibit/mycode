#!/usr/bin/python3
" GBibit Lab 30 Challenge Task"


import zipfile

def main():
    """code"""

    unzip = input("What do you like to unzip?")

    if zipfile.is_zipfile(unzip):
        print("Yes! This is a 'zip' file.")
    else:
        print("No!! This is not a 'zip' file.")


if __name__ == "main__":
    main()


