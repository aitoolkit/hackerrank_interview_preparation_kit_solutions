# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Sol 1
def alternatingCharacters(s):
    if len(s) == 0:
        return 0
    temp = ""
    deletions = 0
    for c in s:
        if c == temp:
            deletions += 1
        else:
            temp = c
    return deletions


# Sol 2
# def alternatingCharacters(s):
#     deletions = 0
    
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             deletions += 1
    
#     return deletions

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = alternatingCharacters(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()