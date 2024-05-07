#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

from ini import set_wd

def tæl_bytes(file):
    counts = [None]*256 #array for effektivitet.
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