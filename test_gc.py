from gc_content import calculate_gc

dna = input("Enter DNA Sequence: ")

result = calculate_gc(dna)

print("\n===== GC Content Analysis =====")
print("Sequence Length :", result["length"])
print(f"GC Content : {result['gc_content']:.2f}%")