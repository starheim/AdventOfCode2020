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

validPassport = False

passports = []
passport = Passport()

for s in textLines:
    if(s != '\n'):
        fields = s.split()
        print(s[:-1])
        print(fields)
        for field in fields:
            print(field)
            entry = field.split(:)
            if entry[0] == 'byr'
                passport.byr == entry[1]
            else if entry[0] == 'iyr'
                passport.iyr == entry[1]
            else if entry[0] == 'eyr'
                passport.eyr == entry[1]
            else if entry[0] == 'hgt'
                passport.iyr == entry[1]
            else if entry[0] == 'hcl'
                passport.iyr == entry[1]
            else if entry[0] == 'ecl'
                passport.iyr == entry[1]
            else if entry[0] == 'pid'
                passport.iyr == entry[1]
            else if entry[0] == 'cid'
                passport.iyr == entry[1]
    else:
        numberOfPassports += 1
        passports.append(passport)
        print(s)
        print("-------------------------------------------------")

print("Number of passports: {}".format(numberOfPassports))
        
