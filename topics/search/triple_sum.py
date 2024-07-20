def triplets(a, b, c):
    
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    
    count = 0
    
    def count_less_equal(arr: list[int], x: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left
    
    for q in b:
        count_a = count_less_equal(a, q)
        count_c = count_less_equal(c, q)
        count += count_a * count_c
    
    return count

# Sol 2 (Greedy)
# def triplets(a, b, c):
#     a.sort()
#     b.sort()
#     c.sort()
    
#     count = 0
#     elements_b = set()
    
#     for q in b:
#         if (q >= a[0]) and (q >= c[0]) and (q not in elements_b):
#             elements_b.add(q)
#             num_el_a = len([x for x in a if x <= q])
#             num_el_c = len([x for x in c if x <= q])
#             count += num_el_a * num_el_c
    
#     print(count)
#     return count