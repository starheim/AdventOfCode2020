textLines = open("Day8/Day8.txt", "r").readlines()

accumulator = 0
lineNumber = 0
linesVisited = []
linesChanged = []
hasTerminated = False
changeMade = False

while lineNumber < len(textLines):
    line = textLines[lineNumber]
    lineInfo = line.rstrip().split(' ')

    if lineNumber in linesVisited:
        print(f"Infinite loop detected, starting over. \nLine number: {lineNumber}, accumulator value: {accumulator}")
        accumulator = 0
        lineNumber = 0
        linesVisited = []
        line = textLines[lineNumber]
        lineInfo = line.rstrip().split(' ')
        changeMade = False
        
    instruction = lineInfo[0]
    argument = int(lineInfo[1])
    linesVisited.append(lineNumber)

    if instruction == 'acc':
        accumulator += argument
        lineNumber += 1
    elif instruction == 'jmp':
        if not changeMade and lineNumber not in linesChanged:
            linesChanged.append(lineNumber)
            lineNumber +=1
            changeMade = True
        else:
            lineNumber += argument
    else:
        if not changeMade and lineNumber not in linesChanged:
            linesChanged.append(lineNumber)
            lineNumber += argument
        else:
            lineNumber += 1

print(f"Boot code completed, accumulator: {accumulator}")
