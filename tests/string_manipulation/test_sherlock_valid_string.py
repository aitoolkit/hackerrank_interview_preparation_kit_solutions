from topics.string_manipulation.sherlock_valid_string import isValid

def test_isValid():
    assert isValid("aabbcd") == "NO"
    assert isValid("aabbccddeefghi") == "NO"
    assert isValid("abcdefghhgfedecba") == "YES"
