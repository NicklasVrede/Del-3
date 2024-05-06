from bitIO import BitReader
from ini import set_wd
from generate_hoffmann import generate_hoffmann
from gen_kodeord import find_stier

#bits at læse 32*256 = 8192 bits
set_wd()
f = open("testOut.txt", "rb")
reader = BitReader(f)

hyppighedstabel = []

for i in range(256):
    hyppighedstabel.append(reader.readint32bits())

print(hyppighedstabel)

rod = generate_hoffmann(hyppighedstabel)

kodeord = find_stier(rod)

#find bits at læse:
sum = sum(hyppighedstabel)

i = 0
#læs mens vi har "hyppigheder" at læse
while i <= sum:
    bitstr = ""
    while (bit := reader.readbit()) != None:
        bitstr += str(bit)
        if bitstr in kodeord:
            i += 1
            break
    
    print(bitstr)