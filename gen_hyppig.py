import numpy as np
from ini import set_wd

def tæl_bytes(file):
    counts = np.zeros(256, dtype=int) #array for effektivitet.
    with open(file, 'rb') as f:
        while (byte := f.read(1)):  #walrus operator assigner f.read(1) til byte.
            counts[byte[0]] += 1  #slice for at få værdien af byte.
            #prøv bincount fra numpy senere.

    return counts

if __name__ == "__main__":
    #set working directory
    set_wd()
    counts = tæl_bytes("test.txt")
    print(counts)