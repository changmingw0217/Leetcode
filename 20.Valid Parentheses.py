class Solution:
    def isValid(self, s: str) -> bool:
        li = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                li.append(char)
            elif char == ')':
                if not li or li[-1] != '(':
                    return False
                li.pop()
            elif char == '}':
                if not li or li[-1] != '{':
                    return False
                li.pop()
            elif char == ']' :
                if not li or li[-1] != '[':
                    return False
                li.pop()
        if len(li) > 0:
            return False
        return True