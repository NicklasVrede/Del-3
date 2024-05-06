from dataclasses import dataclass

class BinNode:
    def __init__(self, nøgle: int):
        self.k: int = nøgle
        self.venstre = None
        self.højre = None

    def __repr__(self) -> str:
        return f"Node({self.frekvens}, {self.unicode})"

    def __lt__(self, other):
        return self.frekvens < other.frekvens  # sammenlign frekvenser

class DictBinTree:
    def __init__(self):
        self.rod = None
    
    def __len__(self):
        return len(self.orderedTraversal())
    
    #Iterativ udgave
    def search(self, k: int) -> bool:
        #Peg på en node  og brug x som i pseudokoden
        x = self.rod

        if x is None:
            return False
        
        if k == x.k:
            return True

        #Søg efter nøglen k
        while x != None and k != x.k:
            if k < x.k:
                x = x.venstre
            else:
                x = x.højre

        if x is None:
            return False
        else:
            return True
        

    def insert(self, k: int) -> None:
        x = self.rod
        y = None
        while x != None:
            y = x
            if k < x.k:
                x = x.venstre
            else:
                x = x.højre

        #y pointer nu på pladsen som k skal indsættes

        if y == None: #Træet er tomt, så k bliver roden
            self.rod = BinNode(k)
        
        elif k < y.k:
            y.venstre = BinNode(k)
        else:
            y.højre = BinNode(k)

    def orderedTraversal(self) -> list[int]:
        res = []
        def træ_gang(x, res=[]):
            if x != None:
                træ_gang(x.venstre, res)
                res.append(x.k)
                træ_gang(x.højre, res)

            return res

        return træ_gang(self.rod)
    
    def extract_min(self):
        #stop hvis træet er tomt
        if self.rod == None:
            return None

        x = self.rod
        y = None

        #find det mindste element
        while x.venstre != None:
            y = x
            x = x.venstre

        #fjern det mindste element
        if y != None:
            y.venstre = x.højre
        else:
            self.rod = x.højre

        return x.k


