fileReader = open("Day3.txt")

textLines = fileReader.readlines()

posX = 0

numberOfTreesHit = 0

width = len(textLines[0])

i = 0

for i in range(0, len(textLines)):

	print(posX)

	if(textLines[i][posX] == '#'):
		print("Character at position {}: {}".format(posX, textLines[i][posX]))
		print("Tree hit! '#rip'")
		numberOfTreesHit += 1

	if posX >= width - 3:
		print("Position reset from {} to {}".format(posX, (posX - (width - 3))))
		print("{} - {} = {}".format(posX, (width - 3), (posX - (width - 3))))
		posX -= width - 3
		print(posX)
	else:
		posX += 3

	print("line number:" + str(i))
	print(textLines[i])
	i += 1

print("Number of trees hit in total {}. Width of lines: {}".format(numberOfTreesHit, width))
