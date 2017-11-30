#this is all the open files code
openDna = open("genomic_dna.txt")
openDnaexon = open("dnaexonfile")
openDnaintron = open("dnaintronfile")
outputDnaexonfile = open("dnaexonfile", "w")
outputDnaintronfile = open("dnaintronfile", "w")

#this is the read the file code
strmyDnafile = openDna.readline()


#this is the spliting the dna code
strmyRna0 = strmyDnafile[:63] + '\n' + strmyDnafile[90:]
strmyRna1 = strmyDnafile[63:90]

#this is the writing to the file code
outputDnaexonfile.write(strmyRna0)
outputDnaintronfile.write(strmyRna1)
outputDnaexonfile.close()
outputDnaintronfile.close()

#reading the files of dna
Dnaexon1 = openDnaexon.readline().strip('\n')
Dnaexon2 = openDnaexon.readline().strip('\n')
Dnaintron = openDnaintron.readline().strip('\n')

#printing the files
print("The first exon is {0} the second exon is {1} and the intron is {2} ".format(Dnaexon1, Dnaexon2, Dnaintron))