from topics.dynamic_programming.abbreviation import abbreviation

def test_abbreviation_YES():
    test_a = "Pi"
    test_b = "P"
    
    assert abbreviation(test_a, test_b) == "YES"

def test_abbreviation_NO():
    test_a = "AfPZN"
    test_b = "APZNC"
    
    assert abbreviation(test_a, test_b) == "NO"