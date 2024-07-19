from topics.search.pairs import pairs

def test_pairs():
    test_arr = [int(num) for num in "1 5 3 4 2".split()]
    test_k = 2
    
    assert pairs(test_k, test_arr) == 3