def twoStrings(s1: str, s2: str) -> str:
    set1 = set(list(s1))
    set2 = set(list(s2))
    is_common_substring = "YES" if set1.intersection(set2) else "NO"
    return is_common_substring

# # Sol 2
# def twoStrings(s1, s2):
#     if len(set(s1) & set(s2)) > 0:
#         return "YES"
#     return "NO"