# I have used the three-letter abbreviations for each amino acid.
# For full names, see http://www.carolguze.com/images/biomolecules/AminoAcidJargonStryerBio3.gif

cStop = ["UAA", "UAG", "UGA"]
codons = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",\
          "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",\
          "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",\
          "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",\
          "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",\
          "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",\
          "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",\
          "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",\
          "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",\
          "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",\
          "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",\
          "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",\
          "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",\
          "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",\
          "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",\
          "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}

# Translates an RNA sequence into amino acids.
# Takes a string of RNA.
# Returns a string of amino acids.
def translate(sequence):
    # find the start codon (AUG) and set the index to begin there
    index = sequence.find("AUG")

    # return error if there is no start codon
    if index < 0:
        return "No start codon found."

    # cut off the sequence before the start codon
    sequence = sequence[index:]

    aminos = ""
    # translate the sequence codon by codon (groups of 3 nucleic acids)
    for i in range(0, len(sequence), 3):
        # break if a stop codon (UAA, UAG, UGA) is encountered
        if sequence[i:i+3] in cStop:
            break
        aminos = aminos + codons[sequence[i:i+3]]

    return aminos

sequence = raw_input("RNA Sequence: ").strip()
print translate(sequence)
