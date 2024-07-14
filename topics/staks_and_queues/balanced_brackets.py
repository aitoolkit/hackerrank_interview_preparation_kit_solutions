# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    brackets = []
    for c in s:
        if (c in [")", "]", "}"]) and (len(brackets) == 0):
            return "NO"
        if (c == ")") and (brackets[-1] == "("):
            brackets.pop(-1)
        elif (c == "]") and (brackets[-1] == "["):
            brackets.pop(-1)
        elif (c == "}") and (brackets[-1] == "{"):
            brackets.pop(-1)
        else:
            brackets.append(c)
    return "YES" if len(brackets) == 0 else "NO"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         s = input()

#         result = isBalanced(s)

#         fptr.write(result + '\n')

#     fptr.close()
