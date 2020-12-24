fileReader = open("Day7/Test.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

bagsContainingShinyGoldBag = []

def bagsContainingBag(bag):
    newBags = []
    for line in textLines:
        lineInfo = line.split(" contain ")
        if bag in lineInfo[1].rstrip():
            newBags.append(lineInfo[0])
    bagsContainingShinyGoldBag.extend(newBags)
    print(f"Found these bags, calling method on: {newBags}")
    for bags in newBags:
        print(f"Called on: {bags}")
        bagsContainingBag(bags)

bagsContainingBag("shiny gold bag")

print(f"\nNumber of times shiny gold bag is contained in another bag: {len(set(bagsContainingShinyGoldBag))}")
print(f"Bags containing shiny gold bag: {set(bagsContainingShinyGoldBag)}")