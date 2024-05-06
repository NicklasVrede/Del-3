from DictBinTree import DictBinTree
from read_hyppighedstabel import count_bytes
import heapq
from ini import set_wd
from graphviz import Digraph

class Element:
    def __init__(self,key,data):
        self.venstre = None
        self.højre = None
        self.key = key
        self.data = data

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.key == other.key

    def __lt__(self,other):
        return self.key < other.key
    
    def __str__(self):
        return f"Element({self.key}, {self.data})"


def generate_hoffmann(hyppighedstabel):
    # Opret en liste af noder
    min_heap = DictBinTree()

    for i, hyppighed in enumerate(hyppighedstabel):
        min_heap.insert(Element(hyppighed, i))

    while len(min_heap) > 1:
        # Fjern de to noder med lavest frekvens
        element_venstre = min_heap.extract_min()
        element_højre = min_heap.extract_min()

        # Opret en ny node med frekvensen lig summen af de to noder
        ny_node = Element(element_venstre.key + element_højre.key, None)
        ny_node.venstre = element_venstre
        ny_node.højre = element_højre

        # Indsæt den nye node i heapen
        min_heap.insert(ny_node)


    # Returner roden af træet
    return min_heap.rod.k


def add_nodes_edges(root, parent_id=None, dot=None):
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
    if parent_id is not None:
        dot.edge(str(parent_id), str(node_id))

    # Recursively add nodes and edges for the left and right children
    add_nodes_edges(root.venstre, node_id, dot)
    add_nodes_edges(root.højre, node_id, dot)

def visualize_tree(root):
    # Create a new Graphviz object
    dot = Digraph(comment='Huffman Tree')

    # Add nodes and edges for the tree
    add_nodes_edges(root, None, dot)

    # Render the Graphviz object
    dot.view()


if __name__ == "__main__":
    set_wd()
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    visualize_tree(rod)
    
    
