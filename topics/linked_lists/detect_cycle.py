class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

def has_cycle(head: Node) -> int:
    nodes = set()
    nodes.add(head)
    current = head
    while (current.next):
        if current.next in nodes:
            return 1
        current = current.next
        nodes.add(current)
    return 0