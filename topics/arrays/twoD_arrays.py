
def hourglassSum(arr):
    max_hg_sum = - float("inf")
    arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
    for i in range(4):
        for j in range(4):
            hg_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if max_hg_sum < hg_sum:
                max_hg_sum = hg_sum
    print(max_hg_sum)
    return max_hg_sum