import re

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

def checkValidity(passport):
    valid = True

    byr = p.passportInfo['byr']
    if not(len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002):
        return False

    iyr = p.passportInfo['iyr']
    if not(len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020):
        return False

    eyr = p.passportInfo['eyr']
    if not(len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030):
        return False

    hgt = p.passportInfo['hgt']
    number = hgt[:-2]
    measurment = hgt[-2:]
    if not(measurment == 'cm' and (150 <= int(number) and int(number) <= 193) or (measurment == 'in' and (59 <= int(number) and int(number) <= 76))):
        return False

    hcl = p.passportInfo['hcl']
    if not(hcl[0] == '#' and re.match("^[a-f0-9]*$", hcl[1:])):
        return False

    legalColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl = p.passportInfo['ecl']
    if not(ecl in legalColors):
        return False

    pid = p.passportInfo['pid']
    if not(len(pid) == 9 and pid.isdigit()):
        return False

    return valid


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
    if(len(p.passportInfo) > 7 or (len(p.passportInfo) == 7 and 'cid' not in p.passportInfo)):
        if(checkValidity(p)):
            numberOfValidPassports += 1

print("Number of passports: {}, number of valid ones: {}".format(numberOfPassports, numberOfValidPassports))
        
