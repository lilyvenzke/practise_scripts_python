'''sentence given. For each letter in sentence determine the postion of letter in alphabet. '''
def alphabet_position(mystring):
    mystring = mystring.upper()
    mystring  = list(mystring)
    alphabet  = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    myindex = []
    for letter in mystring:
        try:
            indexed = alphabet.index(letter) + 1
            myindex.append(str(indexed))
            myindex.append(" ")
        except ValueError:
            myindex.append('')            
    myindex = ''.join(myindex)
    myindex.strip(" ")
    myindex = myindex + '|'
    return myindex
       
mystring = "The sunset sets at twelve o' clock."
print(alphabet_position(mystring))
        
