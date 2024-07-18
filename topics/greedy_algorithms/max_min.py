def maxMin(k, arr):
    arr.sort()
    
    min_unfairness = float("inf")
    
    for i in range(len(arr) - k + 1):
        current_unfairness = arr[i + k - 1] - arr[i]
        
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness
    
    return min_unfairness