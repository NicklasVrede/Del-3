from read_hyppighedstabel import count_bytes
from generate_hoffmann import generate_hoffmann

def find_stier(x) -> list[int]:
    res = dict()
    def træ_gang(x, res, sti=""):
        if x != None:
            træ_gang(x.venstre, res, sti + "0")
            if x.unicode is not None:
                print(f'Nøgle: {x.unicode}, bit-kode: {sti}')
                res["Nøgle: " + str(x.unicode)] = sti
            træ_gang(x.højre, res, sti + "1")

        return res

    return træ_gang(x, res)


if __name__ == "__main__":
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    
    print(find_stier(rod))