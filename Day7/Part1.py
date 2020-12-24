fileReader = open("Day7/Day7.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

bagsContainingShinyGoldBag = []

def contains(bag):
    newBags = []
    for line in textLines:
        lineInfo = line.split(" bags contain ")
        if bag in lineInfo[1].rstrip():
            newBags.append(lineInfo[0])
            print(f"Searching {lineInfo[0]} recursively.")
            contains(lineInfo[0])
    bagsContainingShinyGoldBag.extend(newBags)
    
contains("shiny gold")

print(f"\nNumber of times shiny gold bag is contained in another bag: {len(set(bagsContainingShinyGoldBag))}")
print(f"Bags containing shiny gold bag: {set(bagsContainingShinyGoldBag)}")