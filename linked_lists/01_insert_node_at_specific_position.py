class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of bounds")
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    
    return head

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

# Example Usage:
head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)

data = 4
position = 2

new_head = insertNodeAtPosition(head, data, position)
printLinkedList(new_head)
