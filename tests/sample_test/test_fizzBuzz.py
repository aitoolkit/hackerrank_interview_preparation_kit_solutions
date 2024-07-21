from topics.sample_test.fizzBuzz import fizzBuzz

def test_fizzBuzz():
    test_n = 6
    expected_result = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
    
    assert fizzBuzz(test_n) == expected_result