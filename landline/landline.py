import re

class Landline:
    "Landline is a UK Landline Telephone Number"
    def __init__(self,phoneNumber):
        # sanitise the input and save the input phone number
        self._phoneNumber = self.__removeAllSpaces(phoneNumber)

        # if applicable, remove uk dialing code (+44)
        self.__removeCountryCallingCode()

        # find the grouping format for the given phone number
        self.__findGroupFormat()

        # use the group format to derive pretty print, area code and local code
        self.__applyGroupFormat()

    # Special Methods
    """Public methods with special meaning, these are specific to python"""
    def __str__(self):
        return(self._phoneNumber)

    # Properties
    """Properties are like windows into the Class, they are the numbers and hands on the dial"""
    @property
    def pretty(self):
        return self._prettyFormat

    @property
    def areaCode(self):
        return self._areaCode

    @property
    def localNumber(self):
        return self.__removeAllSpaces(self._localNumber)

    @property
    def format(self):
        return self._groupFormat

    # Private Methods
    """Private Methods are the internals of your Class, the cogs inside the watch"""

    def __removeAllSpaces(self,gappyString):
        return gappyString.replace(" ", "")

    def __removeCountryCallingCode(self):
        if re.search(r"^\+44\d{10}$", self._phoneNumber):
            self._phoneNumber = "0" + self._phoneNumber[3:]
        elif re.search(r"^0044\d{10}$", self._phoneNumber):
            self._phoneNumber = "0" + self._phoneNumber[4:]
        else:
            None

    def __findGroupFormat(self):
        """Use RegEx to parse the phone number, returning a simple string pattern of the number format"""
        """ The complete list of numbers vs patterns:
        01### #####
        01### ######
        011# ### ####
        01#1 ### ####
        013397 #####
        013398 #####
        013873 #####
        015242 #####
        015394 #####
        015395 #####
        015396 #####
        016973 #####
        016974 #####
        016977 ####
        016977 #####
        017683 #####
        017684 #####
        017687 #####
        019467 #####
        019755 #####
        019756 #####
        02# #### ####
        03## ### ####
        05### ######
        07### ######
        0800 ######
        08## ### ####
        09## ### ####
        """

        if re.search(r"^01(3397|3398|3873|5242|5394|5395|5396|6973|6974|6977|7683|7684|7687|9467|9755|9756)\d{5}$", self._phoneNumber):
            self._groupFormat = "6-5"
        elif re.search(r"^011\d{8}$", self._phoneNumber) or re.search(r"^01\d1\d{7}$", self._phoneNumber):
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
        # Exceptionally, two eight digit numbers in use which are not specifically included above: 0800 1111 and 0845 4647
        elif re.search(r"^08001111$", self._phoneNumber) or re.search(r"^08454647$", self._phoneNumber):
            self._groupFormat = "4-4"
        else:
            raise ValueError("Not a valid UK phone number")
        return None

    def __applyGroupFormat(self):
        """Use substringing to split and rebuild the phone number"""
        """ The complete list of patterns:
        11 Digits
            5-6
            4-3-4
            3-4-4
            6-5
        10 Digits
            5-5
            4-6
        8 Digits
            4-4
        """
        if self._groupFormat == "5-6" or self._groupFormat == "5-5":
            self._areaCode = self._phoneNumber[:5]
            self._localNumber = self._phoneNumber[5:]
            self._prettyFormat =  self._areaCode + " " + self._localNumber
        elif self._groupFormat == "4-3-4":
            self._areaCode = self._phoneNumber[:4]
            self._localNumber = self._phoneNumber[4:7] + " " + self._phoneNumber[7:]
            self._prettyFormat =  self._areaCode + " " + self._localNumber
        elif self._groupFormat == "3-4-4":
            self._areaCode = self._phoneNumber[:3]
            self._localNumber = self._phoneNumber[3:7] + " " + self._phoneNumber[7:]
            self._prettyFormat =  self._areaCode + " " + self._localNumber
        elif self._groupFormat == "6-5":
            self._areaCode = self._phoneNumber[:6]
            self._localNumber = self._phoneNumber[6:]
            self._prettyFormat =  self._areaCode + " " + self._localNumber
        elif self._groupFormat == "4-4" or self._groupFormat == "4-6":
            self._areaCode = self._phoneNumber[:4]
            self._localNumber = self._phoneNumber[4:]
            self._prettyFormat =  self._areaCode + " " + self._localNumber
        else:
            raise Exception("Invalid UK Pattern (not 5-6, 4-3-4 etc.)") 

    # Public Methods
    """Public Methods are better for expressing things that either change the state, they are watch's bezel/crown"""
