def oddNumbers(l, r):
    # Write your code here
    odds = []
    
    if l % 2:
        for i in range(l, r + 1, 2):
            odds.append(i)
    else:
        for i in range(l + 1, r + 1, 2):
            odds.append(i)

    return odds

# Which of the following sorting algorithms has the best asymptotic runtime complexity ? Bubble Sort, <Heap Sort>, Selection Sort, Insertion Sort