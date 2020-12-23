from string import ascii_lowercase

fileReader = open("Day6/Day6.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

groupInfo = ""
uniqueCountSum = 0
groupSize = 0

for line in textLines:
    if line != "\n":
        print(line.rstrip())
        groupInfo += line.rstrip()
        groupSize += 1
    else:
        for a in ascii_lowercase:
            if groupInfo.count(a) == groupSize:
                uniqueCountSum += 1

        groupInfo = ""
        groupSize = 0

print(uniqueCountSum)