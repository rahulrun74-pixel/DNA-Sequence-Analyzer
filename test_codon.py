from codon_usage import codon_usage

dna = input("Enter DNA sequence: ")

result = codon_usage(dna)

if result is None:
    print("Invalid DNA Sequence")

else:

    print("\n===== Codon Usage =====")

    for codon, count in sorted(result.items()):
        print(f"{codon} : {count}")