textFile = open("/home/william/Documents/Programming/AdventOfCode2020/TextFiles/Day1/part1.txt", "r")

num = 0;

for i in textFile:
	num += 1

print(num)

for n in textFile:
	num += 1
	for m in textFile:
		print(n + "" + m)
		if n + m == 2020:
			print(n + " +  " + m + " = " + n * m)
