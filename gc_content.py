# GC Content Module

def calculate_gc(dna):
    """
    Calculate GC percentage of a DNA sequence.
    """

    dna = dna.upper()

    # Remove spaces and newlines
    dna = dna.replace(" ", "").replace("\n", "")

    if len(dna) == 0:
        return {
            "gc_content": 0,
            "length": 0
        }

    g = dna.count("G")
    c = dna.count("C")

    gc = ((g + c) / len(dna)) * 100

    return {
        "length": len(dna),
        "gc_content": gc
    }