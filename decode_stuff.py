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

print(f'Hyppighedstabel: {hyppighedstabel}')

#generer kodeord
rod = generate_hoffmann(hyppighedstabel)
kodeord = find_stier(rod)
print(f'Kodeord: {kodeord}')

#find total bits at læse/skrive:
sum = sum(hyppighedstabel)
print(f'Sum af hyppighed: {sum}')

i = 0
bitstrings = []


#læs mens vi har "hyppigheder" at læse
while i < sum:
    bitcode = ""
    current_node = rod
    while current_node.data is None:
        bit = reader.readbit()
        bitcode += str(bit)
        if bit == 0:
            current_node = current_node.venstre
        else:
            current_node = current_node.højre
    bitstrings.append(bitcode)
    i += 1

print(f'Bitstrings: {bitstrings}')

#skriv til fil
