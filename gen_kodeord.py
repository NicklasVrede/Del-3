from read_hyppighedstabel import count_bytes
from generate_hoffmann import generate_hoffmann

def find_stier(x) -> list[int]:
    res = []
    def træ_gang(x, res=[], sti=""):
        if x != None:
            træ_gang(x.venstre, res, sti.append("0"))
            print(f'Nøgle: {x.k}, Sti: {sti}')
            træ_gang(x.højre, res, sti.append("1"))

        return res

    return træ_gang(x)


if __name__ == "__main__":
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    
    print(find_stier(rod))