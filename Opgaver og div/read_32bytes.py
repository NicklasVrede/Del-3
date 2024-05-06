from bitIO import BitReader
from ini import set_wd

set_wd()
f = open("test.txt", "rb")  # Open the file in binary mode
reader = BitReader(f)

# Read 16 bytes from the file as four 32-bit integers
for _ in range(4):
    integer = reader.readint32bits()
    bytes = integer.to_bytes(4, 'big')
    print(f'Integer: {integer},byte1: {bytes[0]}, byte2: {bytes[1]}, byte3: {bytes[2]}, byte4: {bytes[3]}')

f.close()