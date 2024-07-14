
# For each element not in its correct position and not yet visited, follow the cycle to find all elements that are part of the same misplacement cycle.
# Each cycle of length k requires k - 1 swaps to resolve.

def minimumSwaps(arr):
    n = len(arr)
    visited = [False] * n
    index_map = { value: idx for idx, value in enumerate(arr)}
    
    swaps = 0
    
    for i in range(n):
        if visited[i] or arr[i] == i + 1:
            continue
        
        cycle_length = 0
        x = i
        
        while not visited[x]:
            visited[x] = True
            x = index_map[x + 1]
            cycle_length += 1
        
        if cycle_length > 0:
            swaps += cycle_length  - 1
    
    return swaps
