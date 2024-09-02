# Sol 1 : Time consuming

# def minTime(machines, goal):
#     days_min = int(goal / (sum([1/m for m in machines])))
#     days = days_min
#     count = sum([days//machine for machine in machines])
#     while count < goal:
#         days += 1
#         count = sum([days//machine for machine in machines])
#     return days

# Sol 2 : Optimal

def minTime(machines, goal):
    
    left = 1
    
    right = max(machines) * goal
    
    while left < right:
        mid = (left + right) // 2
        total_items = sum(mid // m for m in machines)
    
        if total_items >= goal:
            right = mid
        else:
            left = mid + 1
        
    return left
