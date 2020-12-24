fileReader = open("Day7/Day7.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

bagsContainedInAShinyGoldBag = []

def contains(bag):
    newBags = []
    for line in textLines:
        lineInfo = line.split(" bags contain ")
        containedBags = lineInfo[1].rstrip(".").split(", ")
        if bag in lineInfo[1].rstrip():
            newBags.append()
            contains(lineInfo[0])
    bagsContainedInAShinyGoldBag.extend(newBags)
    
contains("shiny gold")

print(f"\nNumber bags a shiny gold bag holds: {len(bagsContainedInAShinyGoldBag)}")