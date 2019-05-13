#is a number Narsisstic?
# if a digit in a number is multiplied by the number of digits in the whole number
#and all answers is summed to create the same orginal number, then it is a narsisstic number
def narc(value):
    orig_value = value
    value = str(value)
    value = list(value)
    #value = int(value)
    narc = False
    length = len(value)
    answers = []
    for num in value:
        num = int(num)
        num = num**length
        answers.append(num)
    summed = sum(answers)
    if summed == orig_value:
        narc = True
    return narc

print(narc(27))
