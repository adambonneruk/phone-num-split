import logging
from landline import Landline

testdata = [
    # Header Row
    ["input","expected_output","comment"],
    #Test Data
    ["01695571412","01695 571412","Simple 5-6"],
    ["+441695571412","01695 571412","5-6 with a Country Code"],
    ["00441695571412","01695 571412","5-6 with a 00 Country Code"],
    ["01704601501","01704 601501","Another simple 5-6"],
    ["(01695)571412","01695 571412","Brackets"],
    ["0a1d69am5571bon412","01695 571412","Dodgy Characters"],
    ["07765067328","07765 067328","Mobile Number"],
    ["+447765067328","07765 067328","Mobile Number with CC"],
    ["00447765067328","07765 067328","Mobile Number with 00CC"],
    ["01512913000","0151 291 3000","Liverpool 0151 Number"],
    ["+441512913000","0151 291 3000","Liverpool 0151 Number with CC"],
    ["00441512913000","0151 291 3000","Liverpool 0151 Number with 00CC"],
    ["02079460026","020 7946 0026","Simple 020"],
    ["+442079460026","020 7946 0026","020 with CC"],
    ["00442079460026","020 7946 0026","020 with 00CC"],
    ["0 2  0   794 60026","020 7946 0026","020 with Spaces"],
    ["    02$07w946002   6","020 7946 0026","020 with Bad Data"],
    ["01539600000","015396 00000","Rare 6-5 Format"],
    ["+441539600000","015396 00000","Rare 6-5 Format with CC"],
    # Special Cases
    ["08454647","0845 4647","Special 4-4 #1"],
    ["08001111","0800 1111","Special 4-4 #2"],
]

logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.debug("raw test data:\t" + str(testdata))
logging.debug("number of test cases:\t" + str(len(testdata)))

for i in range(1,len(testdata)): #0th test case is the header row
    print(f"Test Case {i}: {testdata[i][2]}")
    print("\tInput String:\t\t" + testdata[i][0])
    print("\tExpected Output:\t" + testdata[i][1])

    try:
        landline = Landline(testdata[i][0])
        assert landline.pretty == testdata[i][1]
        print("\tPassed Assertion:\t" + "Yes" + "\n")
    except:
        print("\nERROR: Test Case", i, "execution halted")
        break
