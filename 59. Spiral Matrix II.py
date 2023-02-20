class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        start_i = start_j = 0
        loop = mid = n // 2
        count = 1
        offset = 1

        while loop > 0:
            i = start_i
            j = start_j

            while j < start_j + n - offset:
                print("i is ", i)
                print("j is ", j)
                result[i][j] = count
                count += 1
                j += 1

                print(result)

            while i < start_i + n - offset:
                print("i is ", i)
                print("j is ", j)
                result[i][j] = count
                count += 1
                i += 1

                print(result)

            while start_j < j:
                print("i is ", i)
                print("j is ", j)
                result[i][j] = count
                count += 1
                j -= 1

                print(result)

            while start_i < i:
                print("i is ", i)
                print("j is ", j)
                result[i][j] = count
                count += 1
                i -= 1

                print(result)

            start_i += 1
            start_j += 1

            offset += 2

            loop -= 1

        if n % 2 == 1:
            result[mid][mid] = n ** 2

        return result


s = Solution()
s.generateMatrix(3)