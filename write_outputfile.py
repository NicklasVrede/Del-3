from generate_hoffmann import generate_hoffmann
from gen_kodeord import find_stier
from read_hyppighedstabel import count_bytes
from bitIO import BitWriter, BitReader
from ini import set_wd


def write_file(hyppighedstabel: dict, original_fil, encoded: str, kodeord:list):
    with open(original_fil, "rb") as f_read, open(encoded, "wb") as f_write:
        writer = BitWriter(f_write)

        #skriv hyppigheder
        for hyppighed in hyppighedstabel:
            writer.writeint32bits(hyppighed)


        #skriv resten af filen
        while (byte := f_read.read(1)):
            for bit in kodeord[byte[0]]:
                writer.writebit(int(bit))


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    kodeord = find_stier(rod)

    
    write_file(hyppighedstabel, "test.txt", "testEncoded.txt", kodeord)

