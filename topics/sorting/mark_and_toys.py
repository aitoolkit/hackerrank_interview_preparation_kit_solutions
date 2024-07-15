def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    money_left = k
    price = 0
    count_toys = 0
    for i in range(len(sorted_prices)):
        if money_left > sorted_prices[i]:
            price = sorted_prices[i]
            money_left -= price
            count_toys += 1
        else:
            print(count_toys)
            return count_toys