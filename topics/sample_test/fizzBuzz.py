from typing import Union

def fizzBuzz(n):
    results: list[Union[int, str]] = []
    for i in range(1, n + 1):
        result: str = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if not result:
            result = str(i)
        
        print(result)
        results.append(result if result != str(i) else i)
    return results

# Which data structure can erase from its beginning or its en in O(1) time ? vector, <deque>, stack, segment tree