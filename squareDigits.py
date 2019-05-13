#square each digit in number and return as a whole number
def squareDigits(digit):
    myDigit = str(digit)
    list(myDigit)
    newList = []
    for num in myDigit:
        num = int(num)
        answer = num * num
        answer = str(answer)
        newList.append(answer)
   # newList = str(newList)
    newList = ''.join(newList)
    newList = int(newList)
    return newList

numbers = 48
print("input: " + str(numbers))
print("output: " + str(squareDigits(numbers)))
