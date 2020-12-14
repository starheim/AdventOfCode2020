class Passport:

	byr = None
	iyr = None
	eyr = None
	hgt = None
	hcl = None
	pid = None
	cid = None

fileReader = open("Day4/Day4.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

numberOfPassports = 0
numberOfValidPassports = 0

passports = None
passport = Passport()

for s in textLines:
    if(s == '\n'):
        numberOfPassports += 1
        print("Number of passports: {}".format(numberOfPassports))
        print(s)
        print("-------------------------------------------------")
    else:
        print(s)

print("Number of passports: {}".format(numberOfPassports))
        
