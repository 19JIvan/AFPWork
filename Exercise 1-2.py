#The DNA sequance
strmyDna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Replacing A with c
strmyRna0 = strmyDna.replace("A", "c")

#Printing to show the steps
print(strmyRna0)

#Replacing C with a
strmyRna1 = strmyRna0.replace("C", "a")

#Printing to show the steps
print(strmyRna1)

#Replacing T with g
strmyRna2 = strmyRna1.replace("T", "g")

#Printing to show the steps
print(strmyRna2)

#Replacing G with t
strmyRna3 = strmyRna2.replace("G", "t")

#Printing to show the steps
print(strmyRna3)

#Printing and changing letters to upper case
print(strmyRna3.upper())