
def checkMagazine(magazine, note):
    m_occurences = {}
    n_occurences = {}
    for word in magazine:
        if word in m_occurences:
            m_occurences[word] += 1
        else:
            m_occurences[word] = 1
    for word in note:
        if word in n_occurences:
            n_occurences[word] += 1
        else:
            n_occurences[word] = 1
    for word in n_occurences:
        if (word not in m_occurences) or (n_occurences[word] > m_occurences[word]):
            print("No")
            return "No"
    print("Yes")
    return "Yes"

# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     m = int(first_multiple_input[0])

#     n = int(first_multiple_input[1])

#     magazine = input().rstrip().split()

#     note = input().rstrip().split()

#     checkMagazine(magazine, note)
