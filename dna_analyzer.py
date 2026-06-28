# dna_analyzer.py

def analyze_dna(dna):
    dna = dna.upper()

    length = len(dna)

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    valid = all(base in "ATGC" for base in dna)

    gc_content = ((g + c) / length * 100) if length > 0 else 0

    return {
        "dna": dna,
        "length": length,
        "A": a,
        "T": t,
        "G": g,
        "C": c,
        "valid": valid,
        "gc_content": gc_content
    }