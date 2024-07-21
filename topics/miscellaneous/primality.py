import math

def primality(n):
    if n <= 1:
        print("Not prime")
        return "Not prime"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Not prime")
            return "Not prime"
    print("Prime")
    return "Prime"