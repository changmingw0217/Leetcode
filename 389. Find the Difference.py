import collections


def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    counter = collections.Counter(s)

    for ch in t:
        if ch not in counter or counter[ch] == 0:
            return ch
        else:
            counter[ch] -= 1


print(findTheDifference("a", "aa"))
