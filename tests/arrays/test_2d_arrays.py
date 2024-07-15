from topics.arrays.twoD_arrays import hourglassSum

def test_hourglassSum():
    test_input = [
        [1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]
    ]
    
    assert hourglassSum(test_input) == 19