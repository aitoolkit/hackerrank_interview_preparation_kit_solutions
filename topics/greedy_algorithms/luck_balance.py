# Sol1
def luckBalance(k, contests):
    important_contests = []
    unimportant_contests = []
    
    for luck, importance in contests:
        if importance == 1:
            important_contests.append(luck)
        else:
            unimportant_contests.append(luck)
    
    important_contests.sort(reverse=True)
    max_luck = sum(unimportant_contests)
    max_luck += sum(important_contests[:k])
    max_luck -= sum(important_contests[k:])
    
    return max_luck


# # Sol2
# def luckBalance(k, contests):
#     tot_luck = 0
#     to_loose = []
#     for luck, imp in contests:
#         tot_luck += luck
#         if imp == 1:
#             to_loose.append(luck)
#     print(tot_luck)
#     to_loose_sorted = sorted(to_loose, reverse=True)
#     # print(to_loose_sorted)
#     for i, luck in enumerate(to_loose_sorted):
#         if i >= k:
#             tot_luck -= 2*luck
#     print(tot_luck)
#     return tot_luck

