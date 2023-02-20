class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {'M': 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        total = 0
        i = 0
        length = len(s)

        while i < length:
            if i + 1 < length and num_dict[s[i]] < num_dict[s[i+1]]:
                total += num_dict[s[i+1]] - num_dict[s[i]]
                i += 2
            else:
                total += num_dict[s[i]]
                i += 1
        return total
