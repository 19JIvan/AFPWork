#open the input file
Dnaneedtrimming = open("ex3-1_input.txt", "r")

#open the output file
dnaTrimmed = open("DnaTrimmed", "w")

#going through the input file one line at a time
for Dna in Dnaneedtrimming:

    #get the posittion of the last character
    lastPosition = len(Dna)

    #trim the substring from the 15th character ton the end of the substring
    trimmedDna = Dna[14:lastPosition]

    #write trimmed dna sequence to output file
    dnaTrimmed.write(trimmedDna)

    #print the length of the trimmed sequence
    print("trimmed dna sequence with length {0}".format(len(trimmedDna)))