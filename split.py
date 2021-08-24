"""split a given uk telephone number into standard area code and local number groups"""
import argparse
import re

def main():
    """main cli-based unix-like tool"""
    #Configure Arguments
    parser = argparse.ArgumentParser(description="Split a UK telephone number into Area Code and Local Number groups",
                                     allow_abbrev=True, #Allows abbreviation if unambiguous
                                     epilog="\"Split\" (Version 0.0.0) by Adam Bonner, 2021"
                                     )
    parser.add_argument('telephonenumber',
                        metavar='<landline-number>',
                        type=str,
                        nargs=1,
                        help="no help")

    args = parser.parse_args()

    print("hello world")
    print(args.telephonenumber)


if __name__ == "__main__":
    main()