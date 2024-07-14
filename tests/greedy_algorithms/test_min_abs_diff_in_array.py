from topics.greedy_algorithms.min_abs_diff_in_array import minimumAbsoluteDifference

def test_minimumAbsoluteDifference():
    test_input_1 = [3, -7, 0]
    test_input_2 = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    test_input_3 = [1, -3, 71, 68, 17]
    
    expected_result_1 = 3
    expected_result_2 = 1
    expected_result_3 = 3
    
    assert minimumAbsoluteDifference(test_input_1) == expected_result_1
    assert minimumAbsoluteDifference(test_input_2) == expected_result_2
    assert minimumAbsoluteDifference(test_input_3) == expected_result_3
    
