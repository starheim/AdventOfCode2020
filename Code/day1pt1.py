##textFile = open("/home/william/Documents/Programming/AdventOfCode2020/TextFiles/Day1/part1.txt", "r")

##numbers = []

##for i in textFile:
##	numbers.append(i)

with open("/home/william/Documents/Programming/AdventOfCode2020/TextFiles/Day1/part1.txt") as f:
	numbers = list(map(str.split, f.read().split('\n')))

print(numbers)

for n in numbers:
	for m in numbers:
		print(n + "" + m + "=" + n+m)
		if n + m == 2020:
			print(n + " " + m + " = " + n * m)
