
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """

        self.available = set(range(maxNumbers))
        self.taken = set()

    def get(self):
        """
        :rtype: int
        """
        if len(self.available) == 0:
            return -1

        number = self.available.pop()
        self.taken.add(number)

        return number

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """

        return number in self.available

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """

        self.taken.discard(number)
        self.available.add(number)

        return None

p = PhoneDirectory(3)
print(p.available)
print(p.get())
print(p.get())
print(p.check(2))

