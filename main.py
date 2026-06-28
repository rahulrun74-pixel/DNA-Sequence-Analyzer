from dna_analyzer import analyze_dna
from gc_content import calculate_gc
from protein_translator import translate_dna
from reverse_complement import reverse_complement
from codon_usage import codon_usage


while True:

    print("\n===================================")
    print("     BIOINFORMATICS TOOLKIT")
    print("===================================")

    print("1. DNA Sequence Analyzer")
    print("2. GC Content Calculator")
    print("3. Protein Translator")
    print("4. Reverse Complement")
    print("5. Codon Usage Analyzer")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        dna = input("Enter DNA Sequence: ")

        result = analyze_dna(dna)

        print("\nDNA Analysis")
        print("Length:", result["length"])
        print("A:", result["A"])
        print("T:", result["T"])
        print("G:", result["G"])
        print("C:", result["C"])
        print(f"GC Content: {result['gc_content']:.2f}%")
        print("Valid:", result["valid"])

    elif choice == "2":

        dna = input("Enter DNA Sequence: ")

        result = calculate_gc(dna)

        print(f"\nGC Content: {result['gc_content']:.2f}%")

    elif choice == "3":

        dna = input("Enter DNA Sequence: ")

        protein = translate_dna(dna)

        print("\nProtein Sequence")
        print(protein)

    elif choice == "4":

        dna = input("Enter DNA Sequence: ")

        rc = reverse_complement(dna)

        print("\nReverse Complement")
        print(rc)

    elif choice == "5":

        dna = input("Enter DNA Sequence: ")

        result = codon_usage(dna)

        if result is None:
            print("Invalid DNA Sequence")
        else:
            print("\nCodon Usage")
            for codon, count in sorted(result.items()):
                print(f"{codon} : {count}")

    elif choice == "6":

        print("\nThank you for using Bioinformatics Toolkit.")
        break

    else:
        print("Invalid choice. Try again.")