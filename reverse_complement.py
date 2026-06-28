# Reverse Complement Module

def reverse_complement(dna):
    """
    Returns the reverse complement of a DNA sequence.
    """

    dna = dna.upper().replace(" ", "").replace("\n", "")

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_comp = ""

    for base in reversed(dna):
        if base in complement:
            reverse_comp += complement[base]
        else:
            return "Invalid DNA sequence"

    return reverse_comp