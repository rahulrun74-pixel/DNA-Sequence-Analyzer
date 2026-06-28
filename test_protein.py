from protein_translator import translate_dna

dna = input("Enter DNA sequence: ")

protein = translate_dna(dna)

print("\nProtein Sequence:")
print(protein)