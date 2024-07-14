from topics.staks_and_queues.balanced_brackets import isBalanced

def test_isBalanced():
    test_input_1 = "{[()]}"
    test_input_2 = "{[(])}"
    test_input_3 = "{{[[(())]]}}"
    
    expected_output_1 = "YES"
    expected_output_2 = "NO"
    expected_output_3 = "YES"
    
    assert isBalanced(test_input_1) == expected_output_1
    assert isBalanced(test_input_2) == expected_output_2
    assert isBalanced(test_input_3) == expected_output_3
