import math;


#sequence to count
strdnaSec = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#counts the number of c's and g's and the length
cAm = strdnaSec.count('C')
gAm = strdnaSec.count('G')
lenAm = len(strdnaSec)

addOfcandg = cAm + gAm
percentOfgc = addOfcandg / lenAm
percentOfgc1 = percentOfgc * 100

print(percentOfgc1)