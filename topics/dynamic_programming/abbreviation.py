def abbreviation(a, b):
    dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    dp[0][0] = True
    
    for i in range(1, len(a) + 1):
        if a[i - 1].islower():
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1].upper() == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            if a[i - 1].islower():
                dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    return "YES" if dp[len(a)][len(b)] else "NO"
                
            