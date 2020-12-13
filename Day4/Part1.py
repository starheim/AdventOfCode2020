class TestClass:
    x = 5

fileReader = open("Day4/Day4.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

blob = TestClass()
numberOfPassports = 0

for s in textLines:
    if(s == '\n'):
        numberOfPassports += 1
        print("Number of passports: {}".format(numberOfPassports))
        print(s)
        print("-------------------------------------------------")
    else:
        print(s)
    if(numberOfPassports > 2):
        break

    
    