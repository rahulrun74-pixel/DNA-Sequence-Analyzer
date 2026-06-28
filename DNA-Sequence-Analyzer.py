#DNA Sequence Analyzer

#get input
dna = input("Enter a DNA Sequence: ")

#Convert to uppercase
dna = dna.upper()


#Gets the length of DNA sequence
length = len(dna)

#count each nucleotide
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

#To check if DNA sequence is Valid
valid = True
for base in dna:
    if base not in "ATGC":
        valid = False
        break

#calculate GC content
if length > 0:
    gc_content = ((g+c) / length) * 100
else:
    gc_content = 0

#display Result
print("\n ========= DNA Sequence Analysis =======")

print("DNA Sequence :", dna)
print("Sequence Length : ", length)

print("\n Nucleotide Count")
print("A :", a)
print("T :", t)
print("G :", g)
print("C :", c)

print(f"\nGC_Content : {gc_content:.2f}%")

if valid:
    print("Valid DNA sequence")
else:
    print("DNA Sequence is not Valid")
