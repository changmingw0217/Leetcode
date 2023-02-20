class MaxStack(object):

    def __init__(self):
        import sys
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_element = -sys.maxsize - 1
        self.max_element_id = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        if x >= self.max_element:
            self.max_element = x
            self.max_element_id = len(self.stack) - 1

    def pop(self):
        """
        :rtype: int
        """
        result = self.stack.pop(-1)
        self.max_element = -sys.maxsize - 1
        for i in range(len(self.stack)):
            if self.stack[i] >= self.max_element:
                self.max_element = self.stack[i]
                self.max_element_id = i

        return result

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_element

    def popMax(self):
        """
        :rtype: int
        """
        result = self.stack.pop(self.max_element_id)
        self.max_element = -sys.maxsize - 1
        for i in range(len(self.stack)):
            if self.stack[i] >= self.max_element:
                self.max_element = self.stack[i]
                self.max_element_id = i

        return result

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()