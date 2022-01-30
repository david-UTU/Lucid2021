numInts = int(input())

newList = []
for i in range(numInts):
    newInput = input()
    newList.append(newInput)

trueCount = 0
if len(newList):
    for x in newList:
        if newList.count(x) > ((len(newList)/3)*2):
            trueCount += 1

if trueCount:
    print(True)
else:
    print(False)

