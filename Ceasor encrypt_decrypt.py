#this is based on a tutorial by Cracking codes with python, just written in my
#own way
print("what message do you want encoded?")#asking for input
message = input()

translated = ''
backTranslated = ''

key = 2 #this doesnt have to be 60, can be any integer between 1 and 26
#all possible letters in my message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?. '
#encoding my message
for letter in message:
    if letter in SYMBOLS:
        #print(letter)    - testing if correct letter is used
        letterIndex = SYMBOLS.find(letter)#find index of letter in message, where it is in SYMBOLS
        newIndex = letterIndex + key #moving index to encode my message
        if newIndex >= len(SYMBOLS):#this handles the wrap around
            newIndex = newIndex - len(SYMBOLS)
        translated = translated + SYMBOLS[newIndex]
    else:
      print('not found in symbols')
      
print(translated)
#testing my encryption by decrypting it to origninal text
print('Decrypt?y/n')
answer = input()
if answer == 'y':
    for transLetter in translated:
        if transLetter in SYMBOLS:
            transLetterIndex = SYMBOLS.find(transLetter)
            newTransIndex = transLetterIndex - key
            if newTransIndex < 0:
                newTransIndex = newTransIndex + len(SYMBOLS)
            backTranslated = backTranslated + SYMBOLS[newTransIndex]
        else:
            print('not found')
print(backTranslated)
            

