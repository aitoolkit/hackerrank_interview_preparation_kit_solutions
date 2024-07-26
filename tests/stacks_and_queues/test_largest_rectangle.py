from topics.staks_and_queues.largest_rectangle import largestRectangle

def test_largest_rectangle():
    test_h1 = [int(x) for x in "1 2 3 4 5".split()]
    test_h2 = [int(x) for x in "1 3 5 9 11".split()]
    test_h3 = [int(x) for x in "11 11 10 10 10".split()]
    
    expected_result_1 = 9
    expected_result_2 = 18
    expected_result_3 = 50
    
    assert largestRectangle(test_h1) == expected_result_1
    assert largestRectangle(test_h2) == expected_result_2
    assert largestRectangle(test_h3) == expected_result_3 