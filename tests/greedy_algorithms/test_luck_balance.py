from topics.greedy_algorithms.luck_balance import luckBalance

def test_luckBalance():
    k = 3
    contests = [
        [5, 1],
        [2, 1],
        [1, 1],
        [8, 1],
        [10, 0],
        [5, 0]
    ]

    assert luckBalance(k, contests) == 29