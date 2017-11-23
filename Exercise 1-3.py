# This is the str that has the DNA code in it
strmyDna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

# finds the length of the str
intmyDnal = len(strmyDna)

# finds the start position of the AATTC and thats the first fragment size
intmyRna1stfrag = strmyDna.find("AATTC")

# this works out the secound fragment size by -'sing the first fragment from the length
intmyRna2ndfrag = intmyDnal - intmyRna1stfrag
print("{0} is the first fragment size and {1} is the secound fragment size".format(intmyRna1stfrag, intmyRna2ndfrag))
