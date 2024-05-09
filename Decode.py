#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23
from bitIO import BitReader
from gen_huffman import gen_huffman
import sys

def decode(kom_fil: str, dekom_fil:str):
    #åbn filen og lav en bitreader
    f = open(kom_fil, "rb")
    reader = BitReader(f)


    #bits at læse 32*256. 
    hyppighedstabel = []
    for _ in range(256):
        hyppighedstabel.append(reader.readint32bits())


    #generer huffman træ
    rod = gen_huffman(hyppighedstabel)

    #tæl mængden af bytes vi skal læse, så vi kan stoppe:
    n_bytes = sum(hyppighedstabel)


    #åbn filen vi skal skrive til
    with open(dekom_fil, "wb") as f:
        #læs n_bytes
        for _ in range(n_bytes):
            #start på roden.
            current_node = rod
            #Gå indtil vi rammer et blad med en byteværdi der ikke er -1.
            while current_node.byteværdi == -1:
                bit = reader.readbit() #Vi læser videre fra efter hyppighederne.
                #retning afhænger af bitværdi
                if bit == 0:
                    current_node = current_node.venstre
                else:
                    current_node = current_node.højre
            
            #Omkonventer byteværdien til en byte og skriv den.
            f.write(bytes([current_node.byteværdi]))

    reader.close() #luk filen


if __name__ == "__main__":
    #sys.argv = ["", "testEncoded.txt", "testDecoded.txt"] #For at teste

    kom_fil = sys.argv[1]
    dekom_fil = sys.argv[2]

    decode(kom_fil, dekom_fil)