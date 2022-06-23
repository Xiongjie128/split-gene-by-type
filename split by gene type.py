
from Bio import SeqIO


# different types of gene
NP = []
PB2 = []
PB1 = []
PA = []
HA = []
NA = []
MP = []
NS = []


# create function to extract sequence

def extract_sequence(filename):
    sequences = [i for i in SeqIO.parse(filename, 'fasta')]
    for sequence in sequences:
        if "NP" in sequence.name:
            NP.append(sequence)

        if "PB2" in sequence.name:
            PB2.append(sequence)

        if "PB1" in sequence.name:
            PB1.append(sequence)

        if "PA" in sequence.name:
            PA.append(sequence)

        if "HA" in sequence.name:
            HA.append(sequence)

        if "NA" in sequence.name:
            NA.append(sequence)

        if "MP" in sequence.name:
            MP.append(sequence)

        if "NS" in sequence.name:
            NS.append(sequence)


extract_sequence('/Users/apple/Desktop/influenza/gisaid_epiflu_sequence.fasta')
extract_sequence('/Users/apple/Desktop/influenza/gisaid_epiflu_sequence2.fasta')



# save as new file
SeqIO.write(NP, '/Users/apple/Desktop/influenza/NP.fasta', 'fasta')
SeqIO.write(PB2, '/Users/apple/Desktop/influenza/PB2.fasta', 'fasta')
SeqIO.write(PB1, '/Users/apple/Desktop/influenza/PB1.fasta', 'fasta')
SeqIO.write(PA, '/Users/apple/Desktop/influenza/PA.fasta', 'fasta')
SeqIO.write(HA, '/Users/apple/Desktop/influenza/HA.fasta', 'fasta')
SeqIO.write(NA, '/Users/apple/Desktop/influenza/NA.fasta', 'fasta')
SeqIO.write(MP, '/Users/apple/Desktop/influenza/MP.fasta', 'fasta')
SeqIO.write(NS, '/Users/apple/Desktop/influenza/NS.fasta', 'fasta')

