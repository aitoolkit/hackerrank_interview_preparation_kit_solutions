def merge_and_count(arr: list[int], temp_arr: list[int], left: int, mid: int, right: int) -> int:
    i = left 
    j = mid + 1
    k = left 
    inv_count = 0
    
    while i <= mid and j<= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def merge_sort_and_count(arr: list[int], temp_arr: list[int], left: int, right: int) -> int:
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    
    return inv_count

def countInversions(arr):
    n = len(arr)
    temp_arr = [0]*n
    return merge_sort_and_count(arr, temp_arr, 0, n-1)
