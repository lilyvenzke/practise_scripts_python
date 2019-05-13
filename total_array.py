''' sum all values in list. return total'''
def sum_array(a):
    total = 0
    i = 0
    for index in a:
        total = total + index
    return total

myList = [5, 5]
print(sum_array(myList))
