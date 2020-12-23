fileReader = open("Day6/Day6.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

groupInfo = ""
uniqueCountSum = 0

for line in textLines:
    if line != "\n":
        print(line.rstrip())
        groupInfo += line.rstrip()
    else:
        uniqueCountSum += len(set(groupInfo))
        print("String: {}, number of unique characters: {}\n".format(groupInfo, len(set(groupInfo))))
        groupInfo = ""

print(uniqueCountSum)
