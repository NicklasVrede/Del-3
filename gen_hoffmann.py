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
        self.venstre = None
        self.højre = None
        self.key = key  # frequency
        self.data = data  # byte value

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

class CoreElement(Element):
    def __init__(self, venstre, højre):
        #Vi vil gerne undgå at merge coreelementer, når vi har elements.
        self.key = venstre.key + højre.key + 0.0000000001# for et mere balanceret træ. Bedre løsning?
        self.data = -1
        self.venstre = venstre
        self.højre = højre
        

def gen_hoffmann(hyppighedstabel):
    # Opret en liste af noder
    min_heap = PQHeap.createEmptyPQ()

    #lav min_heap med små varrierende værdier, for at undgå knuder med samme værdi.
    for i, hyppighed in enumerate(hyppighedstabel):
        PQHeap.insert(min_heap, Element(hyppighed, i))

    # Fjern de to noder med lavest frekvens
    x = PQHeap.extractMin(min_heap)
    while True:
        y = PQHeap.extractMin(min_heap)

        # Hvis der ikke er 2 noder tilbage, så er træet færdigt
        if y is None:
            break

        # Opret en indre knude med x og y som børn
        z = CoreElement(x, y)

        # Indsæt den nye node i heapen
        PQHeap.insert(min_heap, z)

        x = PQHeap.extractMin(min_heap)

    # Returner roden af træet
    return x

def add_nodes_edges(root, parent_id=None, dot=None, edge_label=None):
    # Base case: if the tree is empty, return
    if root is None:
        return

    # Create a unique id for the current node
    node_id = id(root)

    # Create a label for the node
    if isinstance(root, CoreElement):
        label = f"CoreElement\nKey: {root.key}"
    else:
        label = f"Element\nKey: {root.key}\nData: {root.data}"

    # Add the current node to the Graphviz object
    dot.node(str(node_id), label)

    # If this is not the root node, add an edge from the parent node to the current node
    if parent_id is not None and edge_label is not None:
        dot.edge(str(parent_id), str(node_id), label=edge_label)

    # Recursively add nodes and edges for the left and right children
    if isinstance(root, CoreElement):
        add_nodes_edges(root.venstre, node_id, dot, edge_label="0")
        add_nodes_edges(root.højre, node_id, dot, edge_label="1")

def visualize_tree(root):
    # Create a new Graphviz object
    dot = Digraph(comment='Huffman Tree')

    # Add nodes and edges for the tree
    add_nodes_edges(root, None, dot)

    # Render the Graphviz object
    dot.view()


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = tæl_bytes("test.txt")

    rod = gen_hoffmann(hyppighedstabel)
    visualize_tree(rod)
    
    
