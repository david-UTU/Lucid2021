def mainFunc():

    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = []
    sentenceNum = 0
    while True:
        try:
            sentenceNum += 1
            sentence = input()
            if sentence[0] not in capitals:
                output.append(sentenceNum)
            if sentence[-1] != '.':
                output.append(sentenceNum)
            for i in range(len(sentence)-1):
                if sentence[i] == '.':
                    output.append(sentenceNum)
                if sentence[i] == ',' and (i ==0) or (i+1) > len(sentence):
                    output.append(sentenceNum)
                elif sentence[i] == ',' and (((sentence[i-1] not in alphabet) or sentence[i+1] != ' ') or (sentence[i+2] not in alphabet)):
                    output.append(sentenceNum)
                if sentence[i] == ' ':
                    if sentence[i+1] == ' ' or sentence[i-1] == ' ':
                        output.append(sentenceNum)
        except EOFError:
            break
    return output

final = mainFunc()
final = set(final)
if len(final) == 0:
    print('No Problems')
else:
    endString = ''
    for i in final:
        endString += str(i)
        endString += ' '
    endString = endString[:-1]
    print(endString)
