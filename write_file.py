from read_hyppighedstabel import count_bytes
from generate_hoffmann import generate_hoffmann
from gen_kodeord import find_stier
from bitIO import BitWriter

def write_file(kodeord: dict, filnavn: str):
    writer = BitWriter(filnavn)
    with open(filnavn, 'w') as f:
        for nøgle, kode in kodeord.items():
            writer.write(kode)

if __name__ == "__main__":
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    kodeord = find_stier(rod)

    write_file(kodeord, "encoded.txt")

