'''a palindrom: when the sentence/word is the same backwards.  '''
# this program tests my ability to reverse sentences, long and short way
print('What sentence do you want tested for palindrominess?')
sentence = input()
#testing input 
if sentence == '':
    print('no empty lines please! give us a word or sentence you want tested for palindrominess')
    sentence = input('try again: ' )

listSent = list(sentence)
print('this is the short version of reversing my sentences:')
print(sentence)
listSent.reverse()
print(''.join(listSent))
print('')

#can i do this the longway?
print('This is the long method of doing this:')
print(sentence)
listSentTwo = list(sentence)
newSentence = []
i = 0
lengthOfSent = len(listSentTwo)
for i in range (lengthOfSent): #i wrote for letter in sentence,
    # it would stop iterating at position 10. WHY?
    lengthOfSent = len(listSentTwo)
    #print(lengthOfSent)
    #letter = listSent[lengthOfSent - 1:lengthOfSent]
    letter = listSentTwo.pop()
    newSentence.append(letter)
    joinNewSent = ''.join(newSentence)
print(joinNewSent)
#is the sentence a palindrom? i dont know, my computer will tell me
print('is it a palindrome?')
one = joinNewSent.upper()
print(one)
two = sentence.upper()
print(two)
print()
i = 0
counter = 0
for i in range (len(one)):
    if one[i] == two[i]:
        counter = counter + 1
    else:
        counter = counter - 1
    i = i + 1
percentage = (counter/len(one))*100
if percentage == 100:
    print('100 percent match thus a palindrome.')
else:
    print('its not a match thus NOT a palindrome.')









    
