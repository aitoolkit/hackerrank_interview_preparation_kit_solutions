from topics.search.minimum_time_required import minTime

def test_min_time():
    test_machines = [2, 3, 2]
    test_goal = 10
    
    expected_result = 8
    assert minTime(test_machines, test_goal) == expected_result