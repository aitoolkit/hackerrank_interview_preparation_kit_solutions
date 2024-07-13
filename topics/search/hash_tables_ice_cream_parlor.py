def whatFlavors(cost, money):
    cost_dict = {}
    
    for i in range(len(cost)):
        complement = money - cost[i]
        if complement in cost_dict:
            print(cost_dict[complement] + 1, i + 1)
            return cost_dict[complement] + 1, i + 1
        cost_dict[cost[i]] = i