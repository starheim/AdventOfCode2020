fileReader = open('Day2.txt')

textLines = fileReader.readlines()

numberOfValidPasswords = 0

for i in textLines:
	stringSplit = i.split(" ")

	firstPosition = int(stringSplit[0].split("-")[0])
	secondPosition = int(stringSplit[0].split("-")[1])

	letter = stringSplit[1].split(":")[0]
	password = stringSplit[2]

	condition1 = (password[firstPosition-1] == letter)
	condition2 = (password[secondPosition-1] == letter)

	if (not condition1 and condition2) or (condition1 and not condition2):
		numberOfValidPasswords += 1
		print("Password is valid.")

        print("First position: " + str(firstPosition))
        print("Second position: " +  str(secondPosition))
        print("Letter: " + str(letter))
        print("Password: " + str(password))


print("Number of valid passwords: " + str(numberOfValidPasswords))
