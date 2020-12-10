textFile = open('Day1/Day1.txt', 'r')

numberList  = textFile.readlines()

found = False

for n in range(0, len(numberList)):
    for m in range(n + 1, len(numberList)):
        for i in range(m + 1, len(numberList)):
            if int(numberList[n]) + int(numberList[m]) + int(numberList[i]) == 2020:
                found = True
                print("%d + %d + %d = 2020" % (int(numberList[n]), int(numberList[m]), int(numberList[i])))
                print("%d * %d * %d = %d" % (int(numberList[n]), int(numberList[m]), int(numberList[i]), (int(numberList[n]) * int(numberList[m]) * int(numberList[i]))))
                break
        if (found):
            break
    if (found):
        break
            
textFile.close()
