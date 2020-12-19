class Passport:
    filledFields = 0

    content = {}

    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

fileReader = open("Day4/Test.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

numberOfPassports = 0
numberOfValidPassports = 0

passports = []
passport = Passport()

for s in textLines:
    if(s != '\n'):
        fields = s.split()
        for field in fields:
            entry = field.split(":")
            passport.content[entry[0]] = entry[1]
            passport.filledFields += 1
    else:
        numberOfPassports += 1
        passports.append(passport)
        passport = Passport()

numberOfPassports += 1
passports.append(passport)



for p in passports:
    print(p.filledFields)
    print(p.content)
    

print("Number of passports: {}, number of valid ones: {}".format(numberOfPassports, numberOfValidPassports))
        
