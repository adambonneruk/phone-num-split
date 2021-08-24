"""split a given uk telephone number into standard area code and local number groups"""
import argparse
import re

class Landline:
    "Landline is a UK Landline Telephone Number"
    def __init__(self,phoneNumber):
        # sanitise the input and save the input phone number
        self._phoneNumber = self.__removeSpaces(phoneNumber)

        # find the grouping format for the given phone number
        self.__findGroupFormat()

        # use the group format to derive pretty print, area code and local code
        self.__applyGroupFormat()

    # Special Methods
    """Public methods with special meaning, these are specific to python"""
    def __str__(self):
        return(self._groupFormat)

    # Properties
    """Properties are like windows into the Class, they are the numbers and hands on the dial"""
    @property
    def pretty(self):
        return self._phoneNumber

    # Private Methods
    """Private Methods are the internals of your Class, the cogs inside the watch"""
    def __removeSpaces(self,gappyString):
        return gappyString.replace(" ", "")

    def __findGroupFormat(self):
        # based on pattern group, define the grouping format
        if re.search(r"^011\d{8}$", self._phoneNumber) or re.search(r"^01\d1\d{7}$", self._phoneNumber):
            self._groupFormat = "4-3-4"
        elif re.search(r"^01\d{9}$", self._phoneNumber):
            self._groupFormat = "5-6"
        elif re.search(r"^01\d{8}$", self._phoneNumber):
            self._groupFormat = "5-5"
        elif re.search(r"^02\d{9}$", self._phoneNumber):
            self._groupFormat = "3-4-4"
        elif re.search(r"^03\d{9}$", self._phoneNumber):
            self._groupFormat = "4-3-4"
        elif re.search(r"^04\d{9}$", self._phoneNumber):
            raise ValueError("No valid UK phone number starts with 04")
        elif re.search(r"^05\d{9}$", self._phoneNumber):
            self._groupFormat = "5-6"
        elif re.search(r"^06\d{9}$", self._phoneNumber):
            raise ValueError("No valid UK phone number starts with 06")
        elif re.search(r"^07\d{9}$", self._phoneNumber):
            self._groupFormat = "5-6"
        elif re.search(r"^0800\d{6}$", self._phoneNumber):
            self._groupFormat = "4-6"
        elif re.search(r"^08\d{9}$", self._phoneNumber):
            self._groupFormat = "4-3-4"
        elif re.search(r"^09\d{9}$", self._phoneNumber):
            self._groupFormat = "4-3-4"
        else:
            raise ValueError("Not a valid UK phone number")
        return None

    def __applyGroupFormat(self):
        if self._group 5-6
        4-3-4
        3-4-4
        5-5
        4-6

        """
            01### #####
            01### ######
            011# ### ####
            01#1 ### ####
            013397 #####
            013398 #####
            020 #### ####
            03## ### ####
            05### ######
            07### ######
            0800 ######
            08## ### ####
            09## ### ####
        """


    # Public Methods
    """Public Methods are better for expressing things that either change the state, they are watch's bezel/crown"""

    def __str__(self):
        return self._phoneNumber


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

    # print raw input
    print(args.landlinenumber)
    print(args.landlinenumber[0])

    # call Landline class with landline number argument
    mynumber = Landline(args.landlinenumber[0])

    print("----my class----")

    # print formatted number
    print(mynumber)
    print(mynumber.pretty)

if __name__ == "__main__":
    main()