"""split a given uk telephone number into standard area code and local number groups"""
import argparse
import re

class Landline:
    "Landline is a UK Landline Telephone Number"
    def __init__(self,telephoneNumber="999"):
        if telephoneNumber == "999":
            raise ValueError("Number is 999")

        # Object Attributes
        self._wholeNumber = telephoneNumber

    # Properties
    """Properties are like windows into the Class, they are the numbers and hands on the dial"""
    @property
    def wholeNumber(self):
        return self._wholeNumber

    @property
    def areaCode(self):
        return self._areaCode

    @property
    def localNumber(self):
        return self._localNumber

    @property
    def format(self):
        return 

    # Methods
    """Private Methods are the internals of your Class, the cogs inside the watch"""

    # Public Methods
    """Public Methods are better for expressing things that either change the state, they are watch's bezel/crown"""
    def __str__(self):
        return self._wholeNumber


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

    # call Landline class with landline number argument
    foobar = Landline(args.landlinenumber[0])

    # print formatted number
    print(foobar)
    print(foobar.areaCode)
    print(foobar.localNumber)
    print(foobar.split)


if __name__ == "__main__":
    main()