#this is the str of the DNA pattern
strmyDna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

intmyRnal = len(strmyDna)

intmyRna01 = len(strmyDna[:63])
intmyRna02 = len(strmyDna[90:])

intmyRna03 = intmyRna01 + intmyRna02

intmyRna0 =  intmyRna03 / intmyRnal * 100

#this prints the finished product
print(round(intmyRna0, 2))