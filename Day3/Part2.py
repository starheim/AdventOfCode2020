def calculateNumberOfTrees(xMovement, yMovement):

    posX = 0
    width = len(textLines[0]) -1
    numberOfTreesHit = 0

    print("------------------------------")

    for i in range(0, len(textLines), yMovement):
        if(textLines[i][posX] == '#'):
            numberOfTreesHit += 1
        if posX >= width - xMovement:
            posX -= width - xMovement
        else:
            posX += xMovement
        
    print("Toboggan trajectory: {}x, {}y. Number of trees hit: {}".format(xMovement, yMovement, numberOfTreesHit))

    return numberOfTreesHit


fileReader = open("Day3/Day3.txt")
textLines = fileReader.readlines()
fileReader.close()

product = calculateNumberOfTrees(1, 1)

product *= calculateNumberOfTrees(3, 1)

product *= calculateNumberOfTrees(5, 1)

product *= calculateNumberOfTrees(7, 1)

product *= calculateNumberOfTrees(1, 2)

print("------------------------------")
print("Product of all trees hit: {}".format(product))

