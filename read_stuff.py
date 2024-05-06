from bitIO import BitReader
from ini import set_wd
from generate_hoffmann import generate_hoffmann

#bits at læse 32*256 = 8192 bits
set_wd()
f = open("testOut.txt", "rb")
reader = BitReader(f)

res = []

for i in range(256):
    res.append(reader.readint32bits())

print(res)

rod = generate_hoffmann(res)