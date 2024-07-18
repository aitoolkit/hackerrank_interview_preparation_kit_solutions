from topics.greedy_algorithms.max_min import maxMin

def test_maxMin():
    test_arr = [int(x) for x in "10 100 300 200 1000 20 30".split()]
    test_k = 3
    
    assert maxMin(test_k, test_arr) == 20
    