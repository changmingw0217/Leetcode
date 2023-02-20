class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []

        for i in range(n + 1):
            if i == 0:
                continue

            if i % 3 == 0 and i % 5 == 0:
                li.append("FizzBuzz")
            elif i % 3 == 0:
                li.append("Fizz")
            elif i % 5 == 0:
                li.append("Buzz")
            else:
                li.append(str(i))

        return li