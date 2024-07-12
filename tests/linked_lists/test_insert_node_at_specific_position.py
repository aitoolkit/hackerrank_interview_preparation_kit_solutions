from topics.linked_lists.insert_node_at_specific_position import SinglyLinkedListNode, insertNodeAtPosition

# Helper function
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

def test_insert_at_position_0():
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    new_head = insertNodeAtPosition(head, 4, 0)
    assert linkedListToList(new_head) == [4, 1, 2, 3]

def test_insert_at_middle_position():
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    new_head = insertNodeAtPosition(head, 4, 2)
    assert linkedListToList(new_head) == [1, 2, 4, 3]

def test_insert_at_end():
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    new_head = insertNodeAtPosition(head, 4, 3)
    assert linkedListToList(new_head) == [1, 2, 3, 4]
