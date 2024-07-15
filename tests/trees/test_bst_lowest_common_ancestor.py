from topics.trees.bst_lowest_common_ancestor import lca, Node, insert


def setUp() -> Node:
    # Create BST for testing
    root = None
    values = [4, 2, 3, 1, 7, 6]
    for value in values:
        root = insert(root, value)
    return root

def test_lca():
    root = setUp()
    v1, v2 = 1, 7
    result = lca(root, v1, v2)
    assert result.data == 4