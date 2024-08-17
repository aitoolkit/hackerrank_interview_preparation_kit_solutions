
def minTime(machines, goal):
    print(machines)
    print(goal)
    
    days_min = int(goal / (sum([1/m for m in machines])))
    
    days = days_min
    count = sum([days//machine for machine in machines])
    
    while count < goal:
        days += 1
        count = sum([days//machine for machine in machines])
    
    return days
