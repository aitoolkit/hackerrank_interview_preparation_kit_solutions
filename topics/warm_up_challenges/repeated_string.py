def repeatedString(s: str, n: int) -> int:
    # Step 1: Count the number of 'a' in the string `s`
    count_a_in_s = s.count("a")
    
    # Step 2: Calculate the number of full repetitions of `s` within `n`
    full_repetitions = n // len(s)
    
    # Step 3: Calculate the number of 'a's contributed by these full repetitions
    total_count_a = count_a_in_s * full_repetitions
    
    # Step 4: Count the 'a's in the remaining substring
    remaining_chars = n % len(s)
    
    total_count_a += s[:remaining_chars].count("a")
    
    return total_count_a