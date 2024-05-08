#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23
from bitIO import BitReader
from ini import set_wd
from gen_hoffmann import gen_hoffmann
import sys

def decode(kom_fil: str, dekom_fil:str):
    #åben filen og lav en reader
    set_wd()
    f = open(kom_fil, "rb")
    reader = BitReader(f)


    #bits at læse 32*256 = 8192 bits
    hyppighedstabel = []
    for _ in range(256):
        hyppighedstabel.append(reader.readint32bits())


    #generer hoffman træ
    rod = gen_hoffmann(hyppighedstabel)

    #tæl mængden af bytes vi skal læse:
    n_bytes = sum(hyppighedstabel)


    #læs mens vi har "hyppigheder" at læse
    with open(dekom_fil, "wb") as f:
        for _ in range(n_bytes):
            current_node = rod
            while current_node.byteværdi == -1:
                bit = reader.readbit()
                if bit == 0:
                    current_node = current_node.venstre
                else:
                    current_node = current_node.højre
            
            #skriv byten til filen
            f.write(bytes([current_node.byteværdi]))

    reader.close() #luk filen


if __name__ == "__main__":
    sys.argv = ["", "testEncoded.txt", "testDecoded.txt"]

    decode(sys.argv[1], sys.argv[2])