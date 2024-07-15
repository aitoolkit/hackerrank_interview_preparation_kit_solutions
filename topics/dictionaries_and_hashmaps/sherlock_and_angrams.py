from collections import defaultdict
from typing import Any

def sherlockAndAnagrams(s: str) -> int:
    # Dictionary to store the frequency of each sorted substring
    substr_count: Any = defaultdict(int)
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            # Sort the characters of the substring and use it as a key
            sorted_substring = ''.join(sorted(substring))
            substr_count[sorted_substring] += 1
    
    # Calculate the number of anagrammatic pairs
    anagrammatic_pairs = 0
    for count in substr_count.values():
        if count > 1:
            anagrammatic_pairs += (count * (count - 1)) // 2
    return anagrammatic_pairs