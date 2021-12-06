textLines = open("Day9/Test.txt").readlines()

def checkSums(i):

    for n in range(i-5, i-1):
        for m in range(i-4, i-1):
            print(f"{int(textLines[n])} + {int(textLines[m])} = {int(textLines[n]) + int(textLines[m])}. {int(textLines[i])}")
            if int(textLines[n]) != int(textLines[m]) and int(textLines[n]) + int(textLines[m]) == int(textLines[i]):
                print("True")
                return True
                break
    return False
                


for i in range (5, len(textLines)):
    if(not checkSums(i)):
        print(f"Index {i}. {textLines[i].rsplit()} does not have numbers which add up to itself.")
        break
