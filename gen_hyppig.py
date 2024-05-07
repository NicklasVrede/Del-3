#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

from ini import set_wd

def tæl_bytes(file):
    # Opret en liste af 256 elementer, som skal indeholde bitkoderne
    counts = [0]*256

    # Tæl antallet af bytes i filen
    with open(file, 'rb') as f:
        while (byte := f.read(1)):  #:= operator assigner f.read(1) til byte.
            counts[byte[0]] += 1  #slice for at få værdien af byte.

    return counts

if __name__ == "__main__":
    #set working directory
    set_wd()
    counts = tæl_bytes("test.txt")
    print(counts)
    print(f'len(counts): {len(counts)}')