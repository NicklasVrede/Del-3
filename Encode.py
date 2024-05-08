#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

from gen_hoffmann import gen_hoffmann
from gen_kodeord import gen_kodeord
from gen_hyppig import tæl_bytes
from bitIO import BitWriter, BitReader
from ini import set_wd
import time


def write_file(hyppighedstabel: dict, original_fil, encoded: str, kodeord:list):
    with open(original_fil, "rb") as f_read, open(encoded, "wb") as f_write:
        writer = BitWriter(f_write)

        #skriv hyppigheder
        for hyppighed in hyppighedstabel:
            writer.writeint32bits(hyppighed)
        

        total_bitstreng = ""
        #skriv resten af filen
        while (byte := f_read.read(1)):
            bitcode = ""  #for debugging
            for bit in kodeord[byte[0]]: #skriv bitkode på indeks byte[0], bit for bit
                writer.writebit(int(bit))
                bitcode += bit
            total_bitstreng += bitcode

        #luk writer, så den også flusher eventuelle resterende bits
        writer.close()




if __name__ == "__main__":
    set_wd()
    hyppighedstabel = tæl_bytes("test.txt")

    start_time = time.time()
    rod = gen_hoffmann(hyppighedstabel)
    end_time = time.time()
    print(f'Hoffman time = {end_time - start_time}')
    kodeord = gen_kodeord(rod)

    
    write_file(hyppighedstabel, "test.txt", "testEncoded.txt", kodeord)
