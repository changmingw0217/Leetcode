def findMaximizedCapital(k, w, profits, capital):
    """
    :type k: int
    :type w: int
    :type profits: List[int]
    :type capital: List[int]
    :rtype: int
    """
    sum_result = w

    if w >= max(capital):
        sorted_list = sorted(profits, reverse=True)

        for i in range(k+1):
            sum_result += sorted_list[i]

        return sum_result

    n = len(profits)

    for i in range(min(n, k)):
        idx = -1
        for j in range(n):
            if sum_result >= capital[j]:
                if idx == -1:
                    idx = j
                elif profits[j] > profits[idx]:
                    idx = j

        if idx == -1:
            break

        sum_result += profits[idx]
        capital[idx] = float('inf')

    return sum_result


print(findMaximizedCapital(1, 10, [1, 2, 3], [0, 0, 0]))

