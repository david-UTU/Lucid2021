columns = int(input())

order = input().split()

message = input()

lists = []

output = ''

for i in range(0, len(message), columns):
    lists.append(message[i:i+columns])

for j in range(columns):
    for x in order:
        try:
            currList = lists[int(x)-1]
            output += currList[j]
        except IndexError:
            continue
print(output)
