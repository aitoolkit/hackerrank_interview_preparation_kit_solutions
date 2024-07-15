from topics.arrays.left_rotation import rotLeft

def test_rotLeft():
    test_array = "1 2 3 4 5".split()
    num_rot = 4
    expected_output = "5 1 2 3 4".split()
    assert rotLeft(test_array, num_rot) == expected_output