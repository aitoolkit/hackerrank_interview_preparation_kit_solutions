from topics.miscellaneous.friend_circle_queries import maxCircle

def test_maxCircle():
    test_queries = [[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]
    expected_output = [2, 2, 4, 4, 4, 7]
    
    assert maxCircle(test_queries) == expected_output