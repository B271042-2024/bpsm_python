#!/usr/bin/python3

import sys, subprocess

#read file
file = sys.argv[1]

#open file
with open(file) as dnafile:
	content = dnafile.read().rstrip("\n")

#Q1
#extract exon 1
	exon1 = content[0:63]
	print("Exon 1:", exon1,"with length:", len(exon1))

#extract exon 2
	exon2 = content[91:]
	print("Exon 2:", exon2, "with length:", len(exon2))

#Q2
#input 2
	input_2 = input("Type 2 to proceed: ")
	if input_2 != '2':
		print('Exiting...')
	else:
		input_3 = input("Please input the accession ID: ")
#download fasta file
		url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={input_3}&strand=1&rettype=fasta&retmode=text'
		subprocess.call("wget -O", f"{input_3}.fasta", url)
