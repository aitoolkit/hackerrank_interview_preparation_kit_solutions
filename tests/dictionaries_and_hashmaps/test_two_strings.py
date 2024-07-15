from topics.dictionaries_and_hashmaps.two_strings import twoStrings

def test_twoStrings():
    input_s1 = "hello"
    input_s2 = "world"
    input_s3 = "car"
    
    assert twoStrings(input_s1, input_s2) == "YES"
    assert twoStrings(input_s1, input_s3) == "NO"