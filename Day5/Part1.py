def findRow(min, max, reference):
    print("Min: {} \nMax: {} \nReference {}".format(min, max, reference))
    print("Ref len: {}".format(len(reference)))
    if(len(reference)== 1):
        if(reference == 'F'):
            print("Result: {}\n".format(min))
            print("---------------------------")
            return min
        else:
            print("Result: {}\n".format(max))
            print("---------------------------")
            return max
    middle = (max + 1  - min) // 2 + min
    print("Middle: {}\n".format(middle))
    if reference[0] == 'F':
        return findRow(min, middle -1, reference[1:])
    else:
        return findRow(middle, max, reference[1:])


def findColoumn(min, max, reference):
    print("Min: {} \nMax: {} \nReference: {}".format(min, max, reference))
    print("Ref len: {}".format(len(reference)))
    if(len(reference)== 1):
        if(reference == 'L'):
            print("Result: {}\n".format(min))
            print("---------------------------")
            return min
        else:
            print("Result: {}\n".format(max))
            print("---------------------------")
            return max
    middle = (max + 1  - min) // 2 + min
    print("Middle: {}".format(middle))
    if reference[0] == 'L':
        print("L\n")
        return findColoumn(min, middle -1, reference[1:])
    else:
        print("R\n")
        return findColoumn(middle, max, reference[1:])


fileReader = open('Day5/Test.txt', 'r')
textLines = fileReader.readlines()
fileReader.close()

rows = list(range(0, 128))


columns = list(range(0, 8))

n = 3
m = 4
a = [[0] * m for i in range(n)]

for s in textLines:
    row = findRow(0, 127, s.rstrip()[0:7])
    column = findColoumn(0, 7, s.rstrip()[-3:])
    
    print("\nRow: {} \nColumn: {} \nProduct: {} \n".format(row, column, row * 8 + column))