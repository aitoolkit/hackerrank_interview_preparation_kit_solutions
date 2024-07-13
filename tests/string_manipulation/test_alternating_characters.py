from topics.string_manipulation.alternating_characters import alternatingCharacters

# Function to process multiple imputs
def processQueries(inputs):
    results = []
    for s in inputs:
        results.append(alternatingCharacters(s))
    return results

def test_alternating_characters():

    # Sample Input
    inputs = [
        "AAAA",
        "BBBBB",
        "ABABABAB",
        "BABABA",
        "AAABBB"
    ]
    
    expected_results = [
        3,
        4,
        0,
        0,
        4
    ]

    assert expected_results == processQueries(inputs)
