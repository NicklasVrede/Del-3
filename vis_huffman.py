from graphviz import Digraph
from gen_huffman import Node, Element


def add_nodes_edges(rod, parent_id=None, dot=None, edge_label=None):
    # Base case: if the tree is empty, return
    if rod is None:
        return

    # Create a unique id for the current node
    node_id = id(rod)

    # Create a label for the node
    if isinstance(rod, Element):
        label = f"Element\nKey: {rod.key}\nData: {rod.data.byteværdi}"
    else:
        label = f"Node\nByteværdi: {rod.byteværdi}"

    # Add the current node to the Graphviz object
    dot.node(str(node_id), label)

    # If this is not the root node, add an edge from the parent node to the current node
    if parent_id is not None and edge_label is not None:
        dot.edge(str(parent_id), str(node_id), label=edge_label)

    # Recursively add nodes and edges for the left and right children
    if isinstance(rod, Node):
        add_nodes_edges(rod.venstre, node_id, dot, edge_label="0")
        add_nodes_edges(rod.højre, node_id, dot, edge_label="1")

def vis_huffman(rod):
    # Create a new Graphviz object
    dot = Digraph(comment='Huffman Tree')

    # Add nodes and edges for the tree
    add_nodes_edges(rod, None, dot)

    # Render the Graphviz object
    return dot.view()

if __name__ == "__main__":
    from Encode import tæl_bytes
    from gen_huffman import gen_huffman

    
    hyppighedstabel = tæl_bytes("test.txt")

    rod = gen_huffman(hyppighedstabel)
    
    vis_huffman(rod)