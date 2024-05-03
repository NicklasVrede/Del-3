import numpy as np
from ini import set_wd

#set working directory
set_wd()

def count_bytes(file):
    counts = np.zeros(256, dtype=int)
    i = 0
    with open(file, 'rb') as f:
        while (byte := f.read(1)):  #walrus operator assigner f.read(1) til byte.
            print(f'Byte {i}: {byte[0]}') #Vi skal bruge [0] for at få værdien af byte.


count_bytes("test.txt")

