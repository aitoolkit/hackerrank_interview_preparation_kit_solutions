from topics.dictionaries_and_hashmaps.hash_tables_ransom_note import checkMagazine


def test_check_magazine_yes():
    magazine = "give me one grand today night".split()
    note = "give one grand today".split()
    
    assert checkMagazine(magazine, note) == "Yes"


def test_check_magazine_no():
    magazine = "ive got a lovely bunch of coconuts".split()
    note = "ive got some coconuts".split()
    
    assert checkMagazine(magazine, note) == "No"