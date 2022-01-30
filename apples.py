String = input().lower()
newList = [String.count('a'), (String.count('p')/2), String.count('l'), String.count('e')]
print(int(min(newList)))

