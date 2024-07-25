from topics.linked_lists.detect_cycle import has_cycle, Node


def test_has_cycle():
    node1 = Node(1)  # type: ignore
    node2 = Node(2)  # type: ignore
    node3 = Node(3)  # type: ignore
    node4 = Node(4)  # type: ignore
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    assert has_cycle(node1)