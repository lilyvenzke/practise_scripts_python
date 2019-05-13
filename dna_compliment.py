#receives a string with a DNA strand.
#return the complimentary strand
# for A return T (visa versa)
#for C return G (visa versa)
def dna_strand(dna):
    dna = dna.upper()
    dna = list(dna)
    comp = []
    for letter in dna:
        if letter == "A":
            comp.append("T")
        elif letter ==  "T":
            comp.append("A")
        elif letter == "C":
             comp.append("G")
        elif letter == "G":
            comp.append("C")
        else:
            comp.append("")
    comp = ''.join(comp)
    return comp

    
my_dna = "AttGC"
print(dna_strand(my_dna))

# I can also use the following but it makes no allowance for nothing sent or lowercase letters:
''' import string
    def dna_strand(dna):
        return dna.translate(string.maketrans('ATCG', TAGC))

         OR FOR 3.4
         return dna.translate(str.maketrans('ATCG', TAGC))'''
