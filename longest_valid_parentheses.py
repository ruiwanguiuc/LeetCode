class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] denotes the length of the longest valid parentheses substring that ends at i - 1
        dp = [0] * (len(s) + 1)
        maxl = 0

        # starts from 2. dp[1] should be 0 and dp[0] will also be set to 0
        for i in range(2, len(s) + 1):
            if s[i - 1] == '(':
                dp[i] = 0
            else:
                if s[i - 2] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    prev_index = i - 1 - dp[i - 1] - 1
                    if prev_index >= 0 and s[prev_index] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[prev_index]
                    else:
                        dp[i] = 0
            maxl = max(maxl, dp[i])
        return maxl


if __name__ == '__main__':
    print(Solution().longestValidParentheses('()(())'))
    print(Solution().longestValidParentheses('())()'))
