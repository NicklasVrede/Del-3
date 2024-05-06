from read_hyppighedstabel import count_bytes
from generate_hoffmann import generate_hoffmann
from ini import set_wd



def find_stier(x) -> list[int]:
    res = []
    def træ_gang(x, res, sti=""):
        if x != None:
            træ_gang(x.venstre, res, sti + "0")
            if x.data != None:
                res.append(sti)        
            træ_gang(x.højre, res, sti + "1")
        
        return res


    return træ_gang(x, res)


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    
    print(find_stier(rod))