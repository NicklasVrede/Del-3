from bitIO import BitReader
from ini import set_wd
from generate_hoffmann import generate_hoffmann
from gen_kodeord import find_stier

#åben filen og lav en reader
set_wd()
f = open("testEncoded.txt", "rb")
reader = BitReader(f)

#bits at læse 32*256 = 8192 bits
hyppighedstabel = []
for i in range(256):
    hyppighedstabel.append(reader.readint32bits())

#generer kodeord
rod = generate_hoffmann(hyppighedstabel)
kodeord = find_stier(rod)

#find total bits at læse/skrive:
sum = sum(hyppighedstabel)
print(sum)

i = 0
bitstrings = [] 
print(kodeord) 

#læs mens vi har "hyppigheder" at læse
while i <= sum:
    bitstr = ""
    while True:  # Use 'is not None' for clarity
        string = str(reader.readbit())
        bitstr += string
        if bitstr in kodeord:
            i += 1
            break
    print(bitstr)
    bitstrings.append(bitstr)

print(bitstrings)