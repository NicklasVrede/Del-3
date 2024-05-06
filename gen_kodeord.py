from read_hyppighedstabel import count_bytes
from generate_hoffmann import generate_hoffmann
from ini import set_wd
import numpy as np



def find_stier(x) -> list[int]:
    res = [None] * 256
    def træ_gang(x, res, sti=""):
        if x != None:
            træ_gang(x.venstre, res, sti + "0")
            if x.data != None:
                #print(f'Fandt blad med værdi {x.data} og sti {sti}')
                res[x.data] = sti
            træ_gang(x.højre, res, sti + "1")
        
        return res

    return træ_gang(x, res)


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)