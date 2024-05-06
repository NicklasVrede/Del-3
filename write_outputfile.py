from generate_hoffmann import generate_hoffmann
from gen_kodeord import find_stier
from read_hyppighedstabel import count_bytes
from bitIO import BitWriter
from ini import set_wd


def write_file(hyppighedstabel: dict, filnavn: str):
    f = open(filnavn, "wb")
    writer = BitWriter(f)

    #skriv hyppigheder
    for hyppighed in hyppighedstabel:
        writer.writeint32bits(hyppighed)

    #Scan inputfilen igen. Undervejs find for hver byte dets kodeord (ved
    #opslag i tabellen fra punkt 3 over kodeord), og skriv dette kodeords
    #bits til outputfilen.
        
    with open(filnavn, 'rb') as f:
        while (byte := f.read(1)):
            writer.writebit(kodeord[byte[0]])

    

if __name__ == "__main__":
    set_wd()
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    kodeord = find_stier(rod)

    
    write_file(hyppighedstabel, "testEncoded.txt")




    

