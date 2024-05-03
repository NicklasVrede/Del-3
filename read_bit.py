from bitIO import BitReader
from ini import set_wd

set_wd()
f = open("test.txt", "rb")  # Open the file in binary mode
reader = BitReader(f)

# Read bits from the file until there are no more bits
while True:
    bit = reader.readbit()
    if bit is None:  # Check if we've reached the end of the file
        break
    print(bit, end='')

f.close()