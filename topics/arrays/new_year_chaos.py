def minimumBribes(q):
    n = len(q)
    
    bribes = 0
    
    for i in range(n):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return "Too chaotic"
    
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)
    return str(bribes)