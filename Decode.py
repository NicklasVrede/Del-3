#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23
from bitIO import BitReader
from gen_huffman import gen_huffman
import sys

def decode(kom_fil: str, dekom_fil:str):
    #åben filen og lav en reader
    f = open(kom_fil, "rb")
    reader = BitReader(f)


    #bits at læse 32*256 = 8192 bits
    hyppighedstabel = []
    for _ in range(256):
        hyppighedstabel.append(reader.readint32bits())


    #generer hoffman træ
    rod = gen_huffman(hyppighedstabel)

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
    #sys.argv = ["", "testEncoded.txt", "testDecoded.txt"]

    kom_fil = sys.argv[1]
    dekom_fil = sys.argv[2]

    decode(kom_fil, dekom_fil)