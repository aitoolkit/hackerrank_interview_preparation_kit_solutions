from topics.linked_lists.reverse_dll import reverse, DoublyLinkedList, DoublyLinkedListNode

def test_reverse():
    test_llist = DoublyLinkedList()  # type: ignore
    test_llist_items = [1, 3, 4, 10]
    for d in test_llist_items:
        test_llist.insert_node(d)  # type: ignore
    
    llist_1 = reverse(test_llist.head)  # type: ignore
    
    expected_llist = DoublyLinkedList()  # type: ignore
    expected_llist_items = [10, 4, 3, 1]
    for d in expected_llist_items:
        expected_llist.insert_node(d)  # type: ignore
    
    assert llist_1.data == expected_llist.head.data  # type: ignore
    assert llist_1.next.data == expected_llist.head.next.data  # type: ignore
    assert llist_1.next.next.data == expected_llist.head.next.next.data  # type: ignore
    assert llist_1.next.next.next.data == expected_llist.head.next.next.next.data  # type: ignore