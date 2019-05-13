#in a previous program i removed vowels
#here i will replace them with X

sentence = "please replace my vowels with an X"
newSent = ''
VOWEL = 'AEIOUaeiou'

for letter in sentence:
    if letter in VOWEL:
        newSent = newSent + 'X'
    else:
        newSent = newSent + letter
print(newSent)
    
