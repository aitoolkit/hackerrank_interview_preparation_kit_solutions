from topics.search.hash_tables_ice_cream_parlor import whatFlavors

def test_what_flavors():
    test_cases = [
        (4, [1, 4, 5, 3, 2]),
        (4, [2, 2, 4, 3])
    ]

    expected_results = [ (1, 4), (1, 2) ]

    for money, cost in test_cases:
        assert whatFlavors(cost, money) in expected_results
    
    assert whatFlavors(test_cases[0][1], test_cases[0][0]) == expected_results[0]
    assert whatFlavors(test_cases[1][1], test_cases[1][0]) == expected_results[1]