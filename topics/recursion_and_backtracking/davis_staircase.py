def stepPerms(n):
    
    MOD=10000000007
    
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
    
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
    
    return dp[n]