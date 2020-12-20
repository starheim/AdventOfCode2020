class Passport:

    def __init__(self):
        self.filledFields = 0
        self.passportInfo = {}

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
            passport.passportInfo[entry[0]] = entry[1]
            passport.filledFields += 1
    else:
        numberOfPassports += 1
        passports.append(passport)
        passport = Passport()

numberOfPassports += 1
passports.append(passport)

for p in passports:
    if(p.filledFields > 7 or (len(p.passportInfo) == 7 and 'cid' in p.passportInfo)):
        numberOfValidPassports += 1

print("Number of passports: {}, number of valid ones: {}".format(numberOfPassports, numberOfValidPassports))
        
