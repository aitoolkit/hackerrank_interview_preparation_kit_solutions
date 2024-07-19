# Sol 1 (Best performance)
def pairs(k, arr):
    seen = set()
    count = 0
    
    for number in arr:
        if (number - k) in seen:
            count += 1
        if (number + k) in seen:
            count += 1
        seen.add(number)
    
    return count


# # Sol 2 (Time greedy)
# def pairs(k, arr):
#     n_pairs = 0
#     for el in arr:
#         if (el + k) in arr:
#             n_pairs += 1
#     return n_pairs

# # Sol 3 (Optimized)
# def pairs(k, arr):
#     n_pairs = 0
#     dic = {}
#     for el in arr :
#         dic[el] = 1
#     for el in arr:
#         n_pairs += dic.get(el + k, 0)
#     return n_pairs