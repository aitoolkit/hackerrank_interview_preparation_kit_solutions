from topics.warm_up_challenges.repeated_string import repeatedString


def test_repeatedString():
    test_s = "aba"
    test_a = 10
    
    assert repeatedString(test_s, test_a) == 7
