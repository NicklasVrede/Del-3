#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

from ini import set_wd

def tæl_bytes(file):
    # Opret en liste af 256 elementer, som skal indeholde bitkoderne
    counts = [0] * 256

    # Tæl antallet af bytes i filen
    with open(file, 'rb') as f:
        while (byte := f.read(1)):  #:= operator assigner f.read(1) til byte.
            counts[byte[0]] += 1  #Element 0 i byte er byte heltallet.

    return counts
