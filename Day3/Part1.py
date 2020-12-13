fileReader = open("Day3/Day3.txt")
textLines = fileReader.readlines()
fileReader.close()

posX = 0
width = len(textLines[0]) -1
numberOfTreesHit = 0

for i in range(0, len(textLines)):
	if(textLines[i][posX] == '#'):
		numberOfTreesHit += 1
	if posX >= width - 3:
		posX -= width - 3
	else:
		posX += 3

print("Number of trees hit in total: {}".format(numberOfTreesHit))
