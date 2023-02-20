def numKLenSubstrNoRepeats(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = 0
    if len(s) < k:
        return count
    else:
        for i in range(len(s) - k + 1):
            temp_set = set()
            for j in range(k):
                temp_set.add(s[i + j])
            if len(temp_set) == k:
                count += 1
    return count

print(numKLenSubstrNoRepeats("home", 5))