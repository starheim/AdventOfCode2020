fileReader = open('Day2/Day2.txt')

textLines = fileReader.readlines()

numberOfValidPasswords = 0

for i in textLines:
	stringSplit = i.split(" ")

	min = int(stringSplit[0].split("-")[0])
	max = int(stringSplit[0].split("-")[1])

	letter = stringSplit[1].split(":")[0]
	password = stringSplit[2]

	letterUsedTimes = 0

	for s in password:
		if s == letter:
			letterUsedTimes += 1

	if letterUsedTimes >= min and letterUsedTimes <= max:
		numberOfValidPasswords += 1
		print("Password is valid.")

        print("Min number: " + str(min))
        print("Max number: " +  str(max))
        print("Letter: " + str(letter))
        print("Password: " + str(password))


print("Number of valid passwords: " + str(numberOfValidPasswords))
