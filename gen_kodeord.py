#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

from gen_hyppig import tæl_bytes
from gen_hoffmann import gen_hoffmann
from ini import set_wd


def gen_kodeord(x) -> list[int]:
    # Opret en liste af 256 elementer, som skal indeholde bitkoderne
    res = [0] * 256

    # Rekursiv funktion, der går gennem træet og gemmer bitkoderne
    def træ_gang(x, res, sti=""):
        if x is not None and x.data != -1:
            træ_gang(x.venstre, res, sti + "0")
            if x.data != -1:
                res[x.data] = sti
            træ_gang(x.højre, res, sti + "1")
        
        return res

    return træ_gang(x, res)


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = tæl_bytes("test.txt")

    rod = gen_hoffmann(hyppighedstabel)
    
    bitkoder = gen_kodeord(rod)

    print(f'Bitkoder: {bitkoder}')    