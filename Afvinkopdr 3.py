# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:12:28 2016

@author: Sanne Geraets
"""

def main():
    bestand = openbestand()
    seqq = sequentie(bestand)
    seq = sfilter(seqq)
    rna = maak_rna(seq)
#    print(rna)
    codons = create_codons(rna)
#    print(" ".join(codons))
    acids = show_acids(codons)
    print("   ".join(acids))


def openbestand():
    try:
        file = open("m_p53.gb", "r")
        bestand = file.read().upper()
        return bestand
    except IOError:
        print("Er is iets fout gegaan bij het openen van het bestand, probeer het opnieuw.")
    except:
        print("Er is iets fout gedaan.")


def sequentie(bestand):
    seq = bestand.split("ORIGIN")
    return seq[1]


def sfilter(seqq):
    seq1 = []
    for i in seqq:
        if i == "A" or i == "C" or i == "G" or i == "T":
            seq1.append(i)
    seq = "".join(seq1)
    return seq


def maak_rna(seq):
    rna = seq.replace("T","U")
    return rna


def create_codons(rna):
    start = rna.find("AUG")
    done = 0
    codons = []
    print(start)
    if start != -1:
        while start + 2 < len(rna) and done != 1:
            codon = rna[start:start + 3]
            if codon == "UAG" or codon == "UAA" or codon == "UGA":
                done = 1
            if not codon == "UAG" or codon == "UAA" or codon == "UGA":
                codons.append(codon)
                start += 3
    return codons


def show_acids(codons):
    acids = []
#    code = {
#    'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
#    'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
#    'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
#    'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
#    'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
#    'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
#    'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
#    'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
#    'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
#    'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
#    'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
#    'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
#    'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
#    'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
#    'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
#    'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
#    }
    aa3 = {
    "Ala  ": ["GCU", "GCC", "GCA", "GCG"],
    "Arg  ": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Asn  ": ["AAU", "AAC"],
    "Asp  ": ["GAU", "GAC"],
    "Cys  ": ["UGU", "UGC"],
    "Gln  ": ["CAA", "CAG"],
    "Glu  ": ["GAA", "GAG"],
    "Gly  ": ["GGU", "GGC", "GGA", "GGG"],
    "His  ": ["CAU", "CAC"],
    "Ile  ": ["AUU", "AUC", "AUA"],
    "Leu  ": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "Lys  ": ["AAA", "AAG"],
    "Start": ["AUG"],
    "Phe  ": ["UUU", "UUC"],
    "Pro  ": ["CCU", "CCC", "CCA", "CCG"],
    "Ser  ": ["UCU", "UCC", "UCA", "UCG", "AGU","AGC"],
    "Thr  ": ["ACU", "ACC", "ACA", "ACG"],
    "Trp  ": ["UGG"],
    "Tyr  ": ["UAU", "UAC"],
    "Val  ": ["GUU", "GUC", "GUA", "GUG"],
    "Met  ": ["AUG", "CUG", "UUG", "GUG", "AUU"],
    "Stop ": ["UAG", "UGA", "UAA"]
    }
    for x in codons:
        for key in aa3:
            for codon in aa3[key]:
                if x == codon:
#                    acids.append( codon + " " + key)
                    acids.append(key)
    return acids
    
    
main()
