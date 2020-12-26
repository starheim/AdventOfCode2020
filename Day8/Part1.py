textLines = open("Day8/Day8.txt", "r").readlines()

accumulator = 0
lineNumber = 0
linesVisited = []

while lineNumber < len(textLines):
    line = textLines[lineNumber]
    lineInfo = line.rstrip().split(' ')
    argument = int(lineInfo[1])
    
    if lineNumber in linesVisited:
        print(f"Accumulator at start of infinite loop: {accumulator}")
        break
    
    linesVisited.append(lineNumber)

    if lineInfo[0] == 'acc':
        accumulator += argument
        lineNumber += 1
    elif lineInfo[0] == 'jmp':
        lineNumber += argument
    else:
        lineNumber += 1
