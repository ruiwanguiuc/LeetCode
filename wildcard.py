class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp solution similar to edit distance and regex matching. O(m * n)
        # dp[i][j] denotes isMatch(s[i - 1], p[j - 1])
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        # base case
        dp[0][0] = True
        # if p is empty but s is not it's no match so no need to update
        # if s is empty but p is not p has to be all *s to make it a match
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break  # all the following dp[0][j] will be False

        # normal case
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = s[i - 1] == p[j - 1] and dp[i - 1][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().isMatch('aa', 'a') == False
    assert Solution().isMatch('aa', 'aa') == True
    assert Solution().isMatch('aa', '*') == True
    assert Solution().isMatch('aa', 'a*') == True
    assert Solution().isMatch('ab', '?*') == True
    assert Solution().isMatch('aab', 'c*a*b') == False
    assert Solution().isMatch('cddeab', 'c*?a*b') == True
