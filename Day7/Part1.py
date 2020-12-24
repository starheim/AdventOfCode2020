fileReader = open("Day7/Day7.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

bagsContainingShinyGoldBag = []

def contains(bag):
    for line in textLines:
        lineInfo = line.split(" bags contain ")
        if bag in lineInfo[1].rstrip():
            contains(lineInfo[0])
            bagsContainingShinyGoldBag.append(lineInfo[0])
    
contains("shiny gold")

print(f"\nNumber of times shiny gold bag is contained in another bag: {len(set(bagsContainingShinyGoldBag))}")