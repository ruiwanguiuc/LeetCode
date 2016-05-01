class Solution(object):
    def countAndSayNext(self, cur):
        prev = cur[0]
        count = 1
        ret = ''
        for c in cur[1:]:
            if c == prev:
                count += 1
            else:
                ret += str(count) + prev
                prev = c
                count = 1
        ret += str(count) + prev
        return ret

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prev = '1'
        for i in range(n - 1):
            prev = self.countAndSayNext(prev)
        return prev
