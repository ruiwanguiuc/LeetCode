class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.i = 0
        self.j = 0
        self.vec = vec2d

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        ret = self.vec[self.i][self.j]
        if self.j + 1 < len(self.vec[self.i]):
            self.j += 1
            return ret
        self.i += 1
        self.j = 0
        while self.i < len(self.vec):
            if self.j < len(self.vec[self.i]):
                return ret
            else:
                self.i += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.vec):
            if self.j < len(self.vec[self.i]):
                return True
            self.i += 1
            self.j = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


if __name__ == "__main__":
    vec2d = [[1], [3], [4, 5, 6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext():
        # import ipdb; ipdb.set_trace()
        v.append(i.next())
    print v
