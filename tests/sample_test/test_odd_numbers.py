from topics.sample_test.odd_numbers import oddNumbers

def test_oddNumbers():
    input_l = 3
    input_r = 10
    expected_result = [3, 5, 7, 9]
    
    assert oddNumbers(input_l, input_r) == expected_result