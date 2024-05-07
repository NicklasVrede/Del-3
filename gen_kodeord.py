from gen_hyppig import tæl_bytes
from gen_hoffmann import gen_hoffmann
from ini import set_wd
import numpy as np


def gen_kodeord(x) -> list[int]:
    res = [None] * 256 #brug array for effektivitet?
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
    hyppighedstabel = tæl_bytes("test.txt")

    rod = gen_hoffmann(hyppighedstabel)