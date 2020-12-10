textFile = open('Day1/Day1.txt', 'r')

numberList  = textFile.readlines()

found = False

for n in range(0, len(numberList)):
    for m in range(n + 1, len(numberList)):
        if int(numberList[n]) + int(numberList[m]) == 2020:
            found = True
            print("%d + %d = 2020" % (int(numberList[n]), int(numberList[m])))
            print("%d * %d = %d" % (int(numberList[n]), int(numberList[m]), (int(numberList[n]) * int(numberList[m]))))
            break
    if (found):
        break
            
textFile.close()
