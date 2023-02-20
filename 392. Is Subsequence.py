class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_len = len(s)
        t_len = len(t)

        s_index = 0

        if s_len > t_len:
            return False
        if s_len == 0:
            return True

        for i in range(t_len):
            if t[i] == s[s_index]:
                s_index += 1
            if s_index == s_len:
                return True

        return False

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))