#please note that there are a lot of comment out sections, to test my work as
#i write code
print('This is the short method to find and replace all \'o\' to a \'z\'')
sentence = 'fond of oll thos noce'
newSent = ''
newSentence = sentence.replace('o','z')
print(sentence)
print(newSentence)
print(' ')

#the folowing piece of code is to see if i can find the 
#o's without a keyword function like replace
listSent = list(sentence)
#print(listSent) #testing to see if my string to list worked
#listSent = ''.join(listSent)
print('This is the long method:')
print(listSent)
length = len(listSent)
print(length)
for i in range(0, length -1):
    if listSent[i] == 'o':
        listSent.pop(i)
        listSent.insert(i, 'z')
print(''.join(listSent))





    
