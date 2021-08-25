"""split a given uk telephone number into standard area code and local number groups"""
import argparse
from landline import Landline

def main():
    """main cli-based unix-like tool"""
    parser = argparse.ArgumentParser(description="Split a UK telephone number into Area Code and Local Number groups",
                                     allow_abbrev=True, #Allows abbreviation if unambiguous
                                     epilog="\"Split\" (Version 0.0.0) by Adam Bonner, 2021"
                                     )
    parser.add_argument('landlinenumber',
                        metavar='<landline-number>',
                        type=str,
                        nargs=1,
                        help="no help")
    args = parser.parse_args()

    # Raw Input
    print("raw: " + str(args.landlinenumber))

    # Raw Input (Specific Array Input)
    print("ar0: " + args.landlinenumber[0])

    # call Landline class with landline number argument
    landline = Landline(args.landlinenumber[0])

    # print formatted number
    print("num: " + str(landline))
    print("fmt: " + landline.format)
    print("ptt: " + landline.pretty)
    print("std: " + landline.areaCode)
    print("loc: " + landline.localNumber)

if __name__ == "__main__":
    main()