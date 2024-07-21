from topics.miscellaneous.primality import primality

def test_primality():
    test_num = [ int(x) for x in """1
    4
    9
    16
    25
    36
    49
    64
    81
    100
    121
    144
    169
    196
    225
    256
    289
    324
    361
    400
    441
    484
    529
    576
    625
    676
    729
    784
    841
    907""".split("\n")]
    expected_results ="""Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Prime""".split("\n")
    
    results = []
    for i in test_num:
        results.append(primality(i))
    
    assert results == expected_results
    