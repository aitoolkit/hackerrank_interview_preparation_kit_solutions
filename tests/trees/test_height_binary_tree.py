from topics.trees.height_binary_tree import Node, insert, height

def test_height():
    test_values = [3, 5, 2, 1, 4, 6, 7]
    root = None
    for value in test_values:
        root = insert(root, value)
    
    assert height(root) ==3
