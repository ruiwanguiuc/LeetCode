class Solution(object):
    to_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = Solution.to_value[s[-1]]
        res = prev
        for c in reversed(s[:-1]):
            cur = Solution.to_value[c]
            if cur < prev:
                res -= cur
            else:
                res += cur
            prev = cur
        return res


if __name__ == "__main__":
    print(Solution().romanToInt('XCII'))
