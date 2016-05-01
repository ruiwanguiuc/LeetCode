class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] denotes isMatch(s[i - 1], p[j - 1])
        dp = [[False] * (len(p) + 1) for i in range((len(s) + 1))]

        # base case
        dp[0][0] = True
        # p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for j in range(1, len(p) + 1):
            if j >= 2 and p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True
        # dp[i][0] will all be False

        # normal case
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    if p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
                else:
                    # assume p is valid so j >= 2 since p cant be '*'
                    if p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        if s[i - 1] == p[j - 2]:
                            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 2] or dp[i][j - 2]
                        else:
                            dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]


if __name__ == "__main__":
    print Solution().isMatch("aa", "a")  # false
    print Solution().isMatch("aa", "aa")  # true
    print Solution().isMatch("aaa", "aa")  # false
    print Solution().isMatch("aa", "a*")  # true
    print Solution().isMatch("aa", ".*")  # true
    print Solution().isMatch("ab", ".*")  # true
    print Solution().isMatch("aab", "c*a*b")  # true
