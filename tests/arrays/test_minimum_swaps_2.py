from topics.arrays.minimum_swaps_2 import minimumSwaps

def test_minimumSwaps():
    
    test_array_1 = [7, 1, 3, 2, 4, 5, 6]
    test_array_2 = [1, 3, 5, 2, 4, 6, 7]
    
    assert minimumSwaps(test_array_1) == 5
    assert minimumSwaps(test_array_2) == 3