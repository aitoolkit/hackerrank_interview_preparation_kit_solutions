from topics.sorting.merge_sort_counting_inversions import countInversions

def test_countInversions():
    test_input_1 = "1 1 1 2 2".split()
    test_input_2 = "2 1 3 1 2".split()
    
    assert countInversions(test_input_1) == 0
    assert countInversions(test_input_2) == 4