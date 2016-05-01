class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        for i, j in zip(reversed(a), reversed(b)):
            cur = int(i) + int(j) + carry
            if cur == 0:
                res = '0' + res
                carry = 0
            elif cur == 1:
                res = '1' + res
                carry = 0
            elif cur == 2:
                res = '0' + res
                carry = 1
            else:
                res = '1' + res
                carry = 1
        if len(a) > len(b):
            rest = reversed(a[:len(a) - len(b)])
        else:
            rest = reversed(b[:len(b) - len(a)])
        for i in rest:
            cur_sum = int(i) + carry
            if cur_sum == 0:
                res = '0' + res
                carry = 0
            elif cur_sum == 1:
                res = '1' + res
                carry = 0
            else:
                res = '0' + res
                carry = 1
        if carry == 1:
            res = '1' + res
        return res


if __name__ == "__main__":
    print(Solution().addBinary('11', '101'))
