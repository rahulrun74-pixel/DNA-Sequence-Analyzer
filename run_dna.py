from dna_analyzer import analyze_dna
dna = input("Enter a DNA Sequence: ")

result = analyze_dna(dna)

print("\n========= DNA Sequence Analysis =======")

print("DNA Sequence :", result["dna"])
print("Sequence Length :", result["length"])

print("\nNucleotide Count")
print("A :", result["A"])
print("T :", result["T"])
print("G :", result["G"])
print("C :", result["C"])

print(f"\nGC_Content : {result['gc_content']:.2f}%")

if result["valid"]:
    print("Valid DNA sequence")
else:
    print("DNA Sequence is NOT Valid")