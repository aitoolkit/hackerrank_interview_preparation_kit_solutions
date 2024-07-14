# import os

# Sol 1
# def minimumAbsoluteDifference(arr):
#     # Write your code here
#     min_abs = abs(arr[1] - arr[0])
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             min_abs = min(min_abs, abs(arr[i] - arr[j]))
#     print(min_abs)
#     return min_abs


# Sol 2
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_abs = arr[1] - arr[0] # OR min_abs = float('inf)
    for i in range(len(arr) - 1):
        min_abs = min(min_abs, arr[i+1] - arr[i])
    print(min_abs)
    return min_abs

# Sol 3
# def minimumAbsoluteDifference(arr):
#     # Sort the array
#     arr.sort()
    
#     # Initialize the minimum difference with a large value
#     min_diff = float('inf')
    
#     # Iterate through the sorted array and find the minimum absolute difference
#     for i in range(1, len(arr)):
#         diff = abs(arr[i] - arr[i - 1])
#         if diff < min_diff:
#             min_diff = diff
    
#     return min_diff


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = minimumAbsoluteDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
