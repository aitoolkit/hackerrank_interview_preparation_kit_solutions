from topics.arrays.new_year_chaos import minimumBribes

def test_minimumBribes():
    test_q = [int(x) for x in "2 1 5 3 4".split()]
    assert minimumBribes(test_q) == "3"

def test_minimumBribes_chaotic():
    test_q = [int(x) for x in "2 5 1 3 4".split()]
    assert minimumBribes(test_q) == "Too chaotic"