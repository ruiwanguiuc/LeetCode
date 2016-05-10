class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        last = self.stack.pop()
        if last < 0:
            self.min = self.min - last

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:


if __name__ == '__main__':
    stack = MinStack()
    stack.push(2)
    stack.push(1)
    stack.push(3)
    print(stack.top())
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
