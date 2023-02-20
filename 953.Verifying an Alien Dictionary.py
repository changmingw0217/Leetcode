def isAlienSorted(words, order) -> bool:
    order_index = {}
    for i in range(len(order)):
        order_index[order[i]] = i
    print(order_index)

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for_range = min(len(word1), len(word2))

        for j in range(for_range):

            if word1[j] != word2[j]:
                if order_index[word1[j]] > order_index[word2[j]]:
                    return False
                break
        if len(word1) > len(word2) and word1[:for_range] == word2[:for_range]:
            return False
    return True






order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["hello","leetcode"]
isAlienSorted(words,order)