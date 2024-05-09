#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23
import PQHeap


class Element:
    def __init__(self, key, data):
        self.key = key  # frekvens
        self.data = data  # reference til en rod.

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

class Node():
    def __init__(self, byteværdi: int, venstre: 'Node'=None, højre: 'Node'=None):
        self.byteværdi = byteværdi
        self.venstre = venstre
        self.højre = højre


def gen_huffman(hyppighedstabel: list[int]) -> Node:
    # Opret en liste af noder
    min_heap = PQHeap.createEmptyPQ()

    #lav min_heap med elementer
    for byteværdi, hyppighed in enumerate(hyppighedstabel):
        PQHeap.insert(min_heap, Element(hyppighed, Node(byteværdi)))

    
    # Opret et Huffman træ
    for _ in range(255): # Vi skal merge 255 gange.
        # Fjern de to elementer med laveste frekvens
        x = PQHeap.extractMin(min_heap)
        y = PQHeap.extractMin(min_heap)

        # Opret et nyt element med x og y som børn. Vi kunne også genbruge en gammel.
        z = Element(x.key + y.key, Node(-1, x.data, y.data))

        # Indsæt det nye element i heapen
        PQHeap.insert(min_heap, z)

    # Returner roden af træet
    return z.data




    
    
