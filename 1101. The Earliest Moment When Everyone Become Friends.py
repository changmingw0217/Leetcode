class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        logs.sort(key=lambda x: x[0])

        fn = Union(n)

        count = n

        for time, a, b in logs:
            if fn.union(a, b):
                count -= 1
            if count == 1:
                return time

        return -1


class Union(object):

    def __init__(self, n):
        self.group = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, number):
        if self.group[number] != number:
            self.group[number] = self.find(self.group[number])

        return self.group[number]

    def union(self, a, b):

        find_a = self.find(a)
        find_b = self.find(b)

        is_merged = False

        if find_a == find_b:
            return is_merged

        is_merged = True

        rank_a = self.rank[find_a]
        rank_b = self.rank[find_b]

        if rank_a > rank_b:
            self.group[find_b] = find_a

        elif rank_a < rank_b:
            self.group[find_a] = find_b
        else:
            self.group[find_a] = self.group[find_b]
            self.rank[find_b] += 1

        return is_merged


s = Solution()
t = s.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6)
print(t)