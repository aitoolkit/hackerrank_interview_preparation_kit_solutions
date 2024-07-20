from topics.search.triple_sum import triplets

def test_triplets():
    
    test_a = [int(x) for x in "1 3 5".split()]
    test_b = [int(x) for x in "2 3".split()]
    test_c = [int(x) for x in "1 2 3".split()]
    
    assert triplets(test_a, test_b, test_c) == 8


