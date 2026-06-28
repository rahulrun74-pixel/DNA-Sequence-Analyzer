# Codon Usage Analyzer

def codon_usage(dna):
    """
    Counts the occurrence of each codon in a DNA sequence.
    """

    dna = dna.upper().replace(" ", "").replace("\n", "")

    # Validate DNA
    for base in dna:
        if base not in "ATGC":
            return None

    codons = {}

    for i in range(0, len(dna)-2, 3):

        codon = dna[i:i+3]

        if len(codon) == 3:

            if codon in codons:
                codons[codon] += 1
            else:
                codons[codon] = 1

    return codons