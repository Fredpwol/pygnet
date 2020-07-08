
class Node:
    """
    The Node class is used for initializing a node in a graph

    Parameters
        value : int, str or object 
            This is the value of a node object. In graph it is used for identifying
            every node in it.

    Attributes
        value : int, str or object 
        adjecent_nodes : List(Node)
            This is a list of all adjecent node object connected to the node.
    """

    def __init__(self, value, *args, **kwargs):
        self.value = value
        self.adjacent_nodes = []


    def add_node(self, node):
        """
        adds connected node in a graph to the adjecent_nodes list of the Node object.

        Parameters
            node : Node
                node to be added to the list.
        """
        self.adjacent_nodes.append(node)


    def __repr__(self):
        return str(self.value)

    

class Edge:

    def __init__ (self, _from, _to, weight=None, *args, **kwargs):
        self.weight = weight
        self._from = _from
        self._to = _to