import sys
import time

startTime = time.time()

fileReader = open("Day7/Day7.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

bagsContainedInAShinyGoldBag = []

def contains(bag):
    for line in textLines:
        lineInfo = line.split(" bags contain ")
        if lineInfo[0] == bag:
            containedBags = lineInfo[1].rstrip(".\n").split(", ")
            for bag in containedBags:
                if bag[:1].isdigit():
                    numberOfBagType = int(bag[:1])
                    bagType = bag[2:]
                    for i in range(numberOfBagType):
                        bagsContainedInAShinyGoldBag.append(bagType)
                        contains(bagType.rstrip(" bags"))
        
contains("shiny gold")

print(f"\nNumber bags a shiny gold bag holds: {len(bagsContainedInAShinyGoldBag)}")
print(f"Program runtime: {time.time() - startTime}s")
