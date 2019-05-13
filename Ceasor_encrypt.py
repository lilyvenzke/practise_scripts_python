#this program encrypts a line of text
#is reverses the whole text

message = "this is my first message to encrypt"
translated = ""

lengthOfMess = len(message) - 1 #subtract one because we are working with indices
while lengthOfMess >= 0:#we are reversing the message thus >=
    translated = translated + message[lengthOfMess]
    lengthOfMess = lengthOfMess - 1
print(translated)
#decrypt it again
retranslated = ''
lengthOfTrans = len(translated)-1
while lengthOfTrans >= 0:
    retranslated = retranslated + translated[lengthOfTrans]
    lengthOfTrans = lengthOfTrans - 1
print(retranslated)

#ask user for input
newMessage = input('Enter a string:')
newTrans = ''
lengthOfNew = len(newMessage)-1
while lengthOfNew >= 0:
    newTrans = newTrans + newMessage[lengthOfNew]
    lengthOfNew = lengthOfNew - 1
print(newTrans)
    

    
