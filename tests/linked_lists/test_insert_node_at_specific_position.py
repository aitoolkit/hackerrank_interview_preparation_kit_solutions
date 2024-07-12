from topics.linked_lists.insert_node_at_specific_position import SinglyLinkedListNode, insertNodeAtPosition
import unittest

#Helper function
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

# Unit tests
class TestInsertNodeAtPosition(unittest.TestCase):
    
    def setUp(self):
        # Create a sample linked list 1 -> 2 -> 3
        self.head = SinglyLinkedListNode(1)
        self.head.next = SinglyLinkedListNode(2)
        self.head.next.next = SinglyLinkedListNode(3)
    
    def test_insert_at_position_0(self):
        new_head = insertNodeAtPosition(self.head, 4, 0)
        self.assertEqual(linkedListToList(new_head), [4, 1, 2, 3])
    
    def test_insert_at_middle_position(self):
        new_head = insertNodeAtPosition(self.head, 4, 2)
        self.assertEqual(linkedListToList(new_head), [1, 2, 4, 3])
    
    def test_insert_at_end(self):
        new_head = insertNodeAtPosition(self.head, 4, 3)
        self.assertEqual(linkedListToList(new_head), [1, 2, 3, 4])
    