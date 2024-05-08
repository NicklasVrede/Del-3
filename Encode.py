#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

import sys
from gen_hoffmann import gen_hoffmann
from gen_kodeord import gen_kodeord
from gen_hyppig import tæl_bytes
from bitIO import BitWriter
from ini import set_wd


def encode(original_fil, komprimeret_fil):
    #tæl hyppigheder
    hyppighedstabel = tæl_bytes(original_fil)

    #generer hoffman træ
    rod = gen_hoffmann(hyppighedstabel)

    #generer kodeord
    kodeord = gen_kodeord(rod)

    #skriv til fil
    write_file(hyppighedstabel, original_fil, komprimeret_fil, kodeord)



def write_file(hyppighedstabel: dict, original_fil, encoded: str, kodeord:list):
    with open(original_fil, "rb") as f_read, open(encoded, "wb") as f_write:
        writer = BitWriter(f_write)

        #skriv hyppigheder i filen
        for hyppighed in hyppighedstabel:
            writer.writeint32bits(hyppighed)
        

        #skriv resten af filen
        while (byte := f_read.read(1)):
            for bit in kodeord[byte[0]]: #skriv bitkode på indeks byte[0], bit for bit
                writer.writebit(int(bit))

        #luk writer, så den også "flusher" eventuelle resterende bits
        writer.close()


if __name__ == "__main__":
    #set_wd()
    #sys.argv = ["", "test.txt", "testEncoded.txt"]

    original_fil = sys.argv[1]
    komprimeret_fil = sys.argv[2]

    encode(original_fil, komprimeret_fil)

