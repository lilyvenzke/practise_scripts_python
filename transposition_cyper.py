#resource used: invent with python: cracking codes with python book
# transposition ciper encrypt
#move my letters around to encode it. The key shows me where to move the letter
def main():
    myMessage = 'How does this work?'
    print(myMessage)
    myKey = 8

    ciperText = encryptMessage(myKey, myMessage)

    print(ciperText + '|')#| shows end of encryption

def encryptMessage(key, message):
    ciperText = [''] * key

    for colomn in range(key):
        currentIndex = colomn

        
        while currentIndex < len(message):
            ciperText[colomn] = ciperText[colomn] + message[currentIndex]

            currentIndex = currentIndex + key
    return ''.join(ciperText)


#if __name__ == '__main__':
main()
