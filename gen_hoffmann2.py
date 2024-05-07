import heapq
from gen_hyppig import tæl_bytes
from ini import set_wd
from graphviz import Digraph

class Element:
    def __init__(self,key,data):
        self.venstre = None
        self.højre = None
        self.key = key
        self.data = data

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

def gen_hoffmann(hyppighedstabel):
    # Opret en liste af noder
    min_heap = []

    #lav min_heap
    for i, hyppighed in enumerate(hyppighedstabel):
        heapq.heappush(min_heap, Element(hyppighed, i))

    # Fjern de to noder med lavest frekvens
    x = heapq.heappop(min_heap)
    while min_heap:
        y = heapq.heappop(min_heap)

        # Opret en ny node med frekvensen lig summen af de to noder
        z = Element(x.key + y.key, -1)
        z.venstre = x
        z.højre = y

        # Indsæt den nye node i heapen
        heapq.heappush(min_heap, z)

        if min_heap:
            x = heapq.heappop(min_heap)

    # Returner roden af træet
    return x

def add_nodes_edges(root, parent_id=None, dot=None, edge_label=None):
    # Base case: if the tree is empty, return
    if root is None:
        return

    # Create a unique id for the current node
    node_id = id(root)

    # Create a label for the node
    label = f"{root.key}:{root.data}"

    # Add the current node to the Graphviz object
    dot.node(str(node_id), label)

    # If this is not the root node, add an edge from the parent node to the current node
    if parent_id is not None and edge_label is not None:
        dot.edge(str(parent_id), str(node_id), label=edge_label)

    # Recursively add nodes and edges for the left and right children
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