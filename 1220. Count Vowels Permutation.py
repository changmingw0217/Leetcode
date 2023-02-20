class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """

        a_count = [1] * n
        e_count = [1] * n
        i_count = [1] * n
        o_count = [1] * n
        u_count = [1] * n

        Mod = 10 ** 9 + 7

        for i in range(1, n):

            a_count[i] = (e_count[i-1] + i_count[i-1] + u_count[i-1]) % Mod
            e_count[i] = (a_count[i-1] + i_count[i-1]) % Mod
            i_count[i] = (e_count[i-1] + o_count[i-1]) % Mod
            o_count[i] = (i_count[i-1]) % Mod
            u_count[i] = (i_count[i-1] + o_count[i-1]) % Mod

        return (a_count[n-1] + e_count[n-1] + i_count[n-1] + o_count[n-1] + u_count[n-1]) % Mod


s = Solution()
print(s.countVowelPermutation(100))
