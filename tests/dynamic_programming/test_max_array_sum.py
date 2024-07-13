from topics.dynamic_programming.max_array_sum import maxSubsetSum


def test_maxSubsetSum():
    arr0 = [3, 7, 4, 6, 5]
    arr1 = [2, 1, 5, 8, 4]
    arr2 = [3, 5, -7, 8, 10]
    
    assert maxSubsetSum(arr0) == 13
    assert maxSubsetSum(arr1) == 11
    assert maxSubsetSum(arr2) == 15
