def findRow(min, max, reference):
    if(len(reference)== 1):
        if(reference == 'F'):
            return min
        else:
            return max
    middle = (max + 1  - min) // 2 + min
    if reference[0] == 'F':
        return findRow(min, middle -1, reference[1:])
    else:
        return findRow(middle, max, reference[1:])

def findColoumn(min, max, reference):
    if(len(reference)== 1):
        if(reference == 'L'):
            return min
        else:
            return max
    middle = (max + 1  - min) // 2 + min
    if reference[0] == 'L':
        return findColoumn(min, middle -1, reference[1:])
    else:
        return findColoumn(middle, max, reference[1:])

fileReader = open('Day5/Day5.txt', 'r')
textLines = fileReader.readlines()
fileReader.close()

rows = 127
columns = 7
seats = [[0] * (columns+1) for i in range(rows+1)]
answer = 0

for s in textLines:
    row = findRow(0, rows, s.rstrip()[0:7])
    column = findColoumn(0, columns, s.rstrip()[-3:])
    id = row * 8 + column
    if id > answer:
        answer = id
    seats[row][column] = id

seatID = 0

for row in range(rows):
    for column in range(columns):
        if 0 < row and row < rows and 0 < column and column < columns:
            if seats[row][column] == 0 and seats[row][column -1] != 0 and seats[row][column+1] != 0:
                seatID = row * 8 + column

print("My seat: {}\n".format(seatID))

#Print all the seats for show
for rows in seats:
    for columns in rows:
        print(columns,end = " ")
    print()

