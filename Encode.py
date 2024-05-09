#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23
import sys
from gen_huffman import gen_huffman, Node
from bitIO import BitWriter


def tæl_bytes(file: str) -> list[int]:
    # Liste til hyppighederne.
    hyppighedstabel = [0] * 256 #Array ikke tiladt :(

    # Tæl antallet af bytes i filen
    with open(file, 'rb') as f:
        while (byte := f.read(1)):  #:= operator assigner f.read(1) til byte.
            hyppighedstabel[byte[0]] += 1  #Element 0 i byte er byte heltallet.

    return hyppighedstabel

def gen_kodeord(x: Node) -> list[int]:
    # Opret en liste af 256 elementer til bitkoderne
    bitkoder = [0] * 256

    # Rekursiv funktion, der går gennem træet og laver bitkoderne undervejs.
    def træ_gang(x: Node, bitkoder: list, sti: str=""):
        # Stop og opdater bitkoden hvis vi er nået til et blad.
        if x.byteværdi != -1:
            bitkoder[x.byteværdi] = sti #Opdater den specifikke bitkode.

        #Ellers går vi videre:
        else:
            træ_gang(x.venstre, bitkoder, sti + "0")
            træ_gang(x.højre, bitkoder, sti + "1")
        
        
    træ_gang(x, bitkoder) #Start rekursionen og opdater bitkoderne.
    return bitkoder

def write_file(hyppighedstabel: list, org_fil: str, komp_fil: str, kodeord: list):
    with open(org_fil, "rb") as f_read, open(komp_fil, "wb") as f_write:
        writer = BitWriter(f_write)

        #skriv hyppigheder i filen
        for hyppighed in hyppighedstabel:
            writer.writeint32bits(hyppighed) #32 bits for hver hyppighed.
        

        #skriv resten af filen
        while (byte := f_read.read(1)):
            for bit in kodeord[byte[0]]: #skriv bitkode på indeks byte[0], bit for bit
                writer.writebit(int(bit))

        #luk writer, så den "flusher" eventuelle resterende bits
        writer.close()


def encode(org_fil: str, komp_fil: str):
    #tæl hyppigheder
    hyppighedstabel = tæl_bytes(org_fil)

    #generer hoffman træ
    rod = gen_huffman(hyppighedstabel)

    #generer kodeord
    kodeord = gen_kodeord(rod)

    #skriv til fil
    write_file(hyppighedstabel, org_fil, komp_fil, kodeord)


if __name__ == "__main__":
    #sys.argv = ["", "test.txt", "testEncoded.txt"] #For at teste

    original_fil = sys.argv[1]
    komprimeret_fil = sys.argv[2]

    encode(original_fil, komprimeret_fil)

