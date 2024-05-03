from DictBinTree import DictBinTree
from read_hyppighedstabel import count_bytes
import heapq
from graphviz import Digraph


class Node:
    def __init__(self, k: int):
        self.frekvens = k
        self.unicode = None #Måske?
        self.venstre = None
        self.højre = None

    def __repr__(self) -> str:
        return f"Node({self.frekvens}, {self.unicode})"

    def __lt__(self, other):
        return self.frekvens < other.frekvens  # sammenlign frekvenser


def generate_hoffmann(hyppighedstabel):
    # Opret en liste af noder
    noder = []
    
    for index, k in enumerate(hyppighedstabel):
        if k > 0:
            node = Node(k)
            node.unicode = index
            noder.append(node)
    
    print(noder)

    heapq.heapify(noder)

    while len(noder) > 1:
        x = heapq.heappop(noder)
        y = heapq.heappop(noder)

        z = Node(x.frekvens + y.frekvens)
        z.venstre = x
        z.højre = y

        heapq.heappush(noder, z)

    return noder[0]  # Returner roden af træet


def visualize_tree(root):
    dot = Digraph(comment='Huffman Tree')

    def add_nodes_edges(root, parent_id=None, dot=None, sti=""):
        # Check if the node is a leaf
        is_leaf = root.venstre is None and root.højre is None

        # Change the color of the node based on whether it's a leaf
        node_color = 'black' if is_leaf else 'red'

        # Change the label of each node to display the unicode value, the frequency, and the path
        label = f'"{chr(root.unicode)}":{root.frekvens} ({sti})' if root.unicode is not None else str(root.frekvens)
        dot.node(str(id(root)), label, color=node_color)

        if parent_id is not None:
            dot.edge(parent_id, str(id(root)))

        if root.venstre is not None:
            add_nodes_edges(root.venstre, str(id(root)), dot=dot, sti=sti+"0")
        if root.højre is not None:
            add_nodes_edges(root.højre, str(id(root)), dot=dot, sti=sti+"1")

    add_nodes_edges(root, dot=dot)
    dot.view()


if __name__ == "__main__":
    hyppighedstabel = count_bytes("test.txt")

    rod = generate_hoffmann(hyppighedstabel)
    visualize_tree(rod)