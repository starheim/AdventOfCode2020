class Passport:

    def __init__(self):
        self.passportInfo = {}

fileReader = open("Day4/Day4.txt", "r")
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
    else:
        numberOfPassports += 1
        passports.append(passport)
        passport = Passport()

numberOfPassports += 1
passports.append(passport)

for p in passports:
    valid = True
    if(len(p.passportInfo) > 7 or (len(p.passportInfo) == 7 and 'cid' not in p.passportInfo)):
        numberOfValidPassports += 1

print("Number of passports: {}, number of valid ones: {}".format(numberOfPassports, numberOfValidPassports))
        
