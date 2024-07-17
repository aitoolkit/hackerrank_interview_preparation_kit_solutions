
# Sol 1
def isValid(s):
    # freq = {}
    # for c in s:
    #     freq[c] = freq.get(c, 0) + 1
    # diff = list(freq.values())[0]
    # num_diff = 0
    # print(freq)
    # freq1 = 0
    # freq2 = 0
    # for c in freq:
    #     if (abs(freq[c] - diff) == 1):
    #         num_diff += 1
    #     if (abs(c - diff) > 1) or (num_diff > 1):
    #         return "NO"
    # return "YES"
    # Step 1: Count the frequency of each character
    char_count: dict[str, int] = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    freq_count: dict[int, int] = {}
    for count in char_count.values():
        if count in freq_count:
            freq_count[count] += 1
        else:
            freq_count[count] = 1
    
    if len(freq_count) == 1:
        return "YES"
    elif len(freq_count) == 2:
        freq1, freq2 = list(freq_count.keys())
        count1, count2 = freq_count[freq1], freq_count[freq2]
        
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return "YES"
        
        if (abs(freq1 - freq2) == 1) and ((freq1 > freq2 and count1 == 1) or (freq2 > freq1 and count2 == 1)):
            return "YES"
    
    return "NO"


# # Sol 2
# def isValid(s):
#     from collections import Counter
    
#     # Count the frequency of each character
#     char_count = Counter(s)
    
#     # Count the frequencies of these frequencies
#     freq_count = Counter(char_count.values())
    
#     if len(freq_count) == 1:
#         return "YES"
    
#     elif len(freq_count) == 2:
#         freq1, freq2 = list(freq_count.keys())
#         count1, count2 = freq_count[freq1], freq_count[freq2]
        
#         if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
#             return "YES"
        
#         if (abs(freq1 - freq2) == 1) and ((freq1 > freq2 and count1 == 1) or (freq2 > freq1 and count2 == 1)):
#             return "YES"
    
#     return "NO"