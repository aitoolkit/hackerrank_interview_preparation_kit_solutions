from topics.dynamic_programming.candies import candies

def test_candies():
    
    assert candies(3, [1, 2, 2]) == 4
    assert candies(3, [1, 2, 3]) == 6
    assert candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1])
    assert candies(8, [2, 4, 3, 5, 2, 6, 4, 5])