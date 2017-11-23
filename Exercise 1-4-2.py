#this is the str of the DNA pattern
strmyDna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#this splits the intron
strmyRna = strmyDna[63:90]

#this prints the finished product
print(strmyDna[:63] + strmyRna.lower() + strmyDna[90:])