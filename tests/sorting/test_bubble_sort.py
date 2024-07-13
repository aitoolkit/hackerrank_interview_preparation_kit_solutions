from  topics.sorting.bubble_sort import countSwaps


def test_count_swaps():
    # Having
    a = [6, 4, 1]
    expected_result = [1, 4, 6]
    # When
    result = countSwaps(a)
    # Then
    assert result == expected_result
