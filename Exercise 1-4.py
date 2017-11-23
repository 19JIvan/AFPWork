#this is the str of the DNA pattern
strmyDna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#this splits the code for the first and secound coding region
strmyRna0 = strmyDna[:63] + ' this is the first coding region and ' + strmyDna[91:] + ' is the secound coding region'

#this prints the finished product
print(strmyRna0)