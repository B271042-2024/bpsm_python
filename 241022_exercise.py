#!/usr/bin/python3

#1
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("Query: ", dna)
basea = dna.count("A")
baset = dna.count("T")
final = (basea + baset) / len(dna)
print(basea)
print(baset)
print(str(final)+", or " + str(int(final*100)) + "%")

#2
base1 = dna.replace("A","t")
base2 = base1.replace("T","a")
base3 = base2.replace("G","c")
base4 = base3.replace("C","g")
print("Complement DNA: ", base4.upper())

#3
dna2="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = dna2.find("GAATTC")
print("1 Position of the motif, GAATTC: ", motif)
poscut = dna2.find("AATTC")
print("2 Position of the AATTC: ", poscut)
print("3 Length of second fragment: ", len(dna2[poscut:]))

#4
dna3="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print("DNA: ", dna3)
exon_1 = dna3[:63]
exon_2 = dna3[90:]
sum = exon_1 + exon_2
print("Coding region: ", sum)

#5
sumprop = len(sum)
allprop = len(dna3)
perc = sumprop/allprop*100
print("% coding DNA Sequences: ", str(perc) + "%")

#6
intron = dna3[63:90]	#the first number is included, the last number is not included (index starts with 0)
print("DNA Sequence: ", exon_1 + intron.lower() + exon_2)
