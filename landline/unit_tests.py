from landline import Landline

unittests = [   "01695571988",
                "+441695571988",
                "00441695571988",
                "07765067328",
                "016 955 71988",
                "01704501302",
                "01512 913001",
                "0044 20 7946 0026",
                "+44 20 7946 0026",
                "0151      291 300 1",
                "   + 44  151      291 300 1    ",
                "08454647",
                "08001111",
                "(+44)  (20)79460p018"
            ]

#initialise object array for Landline class
landline = []

for i in range(len(unittests)):
    print("\nTest " + str(i+1) + "\n-------------------")
    print("Input:\t" + unittests[i])
    landline.append(Landline(unittests[i]))
    print("Output:\t" + landline[i].pretty)
