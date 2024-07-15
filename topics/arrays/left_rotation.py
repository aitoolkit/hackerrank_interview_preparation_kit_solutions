def rotLeft(a: list[int], d: int) -> list[int]:
    new_array = [0] * len(a)
    for i in range(len(a)):
        new_array[(i - d) % len(a)] = a[i]
    return new_array
