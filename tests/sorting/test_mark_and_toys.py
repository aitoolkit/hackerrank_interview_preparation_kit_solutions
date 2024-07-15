from topics.sorting.mark_and_toys import maximumToys

def test_maximumToys():
    test_prices =[1, 12, 5, 111, 200, 1000, 10]
    test_budget = 50
    
    assert maximumToys(test_prices, test_budget)