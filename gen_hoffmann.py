#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23

import PQHeap
from gen_hyppig import tæl_bytes
from ini import set_wd
from graphviz import Digraph

class Element:
    def __init__(self, key, data):
        self.key = key  # frekvens
        self.data = data  # byte værdi

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

class Node():
    def __init__(self, byteværdi, venstre, højre):
        self.byteværdi = byteværdi
        self.venstre = venstre
        self.højre = højre


def gen_hoffmann(hyppighedstabel):
    # Opret en liste af noder
    min_heap = PQHeap.createEmptyPQ()

    #lav min_heap med elementer
    for i, hyppighed in enumerate(hyppighedstabel):
        PQHeap.insert(min_heap, Element(hyppighed, Node(i, None, None)))

    
    # Opret et Huffman træ
    for _ in range(255):
        # Fjern de to noder med lavest frekvens
        x = PQHeap.extractMin(min_heap)
        y = PQHeap.extractMin(min_heap)

        # Opret en indre knude med x og y som børn
        z = Element(x.key + y.key, Node(-1, x.data, y.data))

        # Indsæt den nye node i heapen
        PQHeap.insert(min_heap, z)

    # Returner roden af træet
    return z.data


if __name__ == "__main__":
    from vis_hoffmann import visualize_tree
    set_wd()
    hyppighedstabel = tæl_bytes("test.txt")

    rod = gen_hoffmann(hyppighedstabel)
    
    visualize_tree(rod)
    
    
