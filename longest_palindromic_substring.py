class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if (r - l + 1) > Solution.max_length:
                Solution.max_length = r - l + 1
                Solution.max_l, Solution.max_r = l, r

        Solution.max_length = 0
        Solution.max_l = -1
        Solution.max_r = -1
        for i in xrange(len(s)):
            expand(i, i)  # in case palindrome is odd length
            expand(i, i + 1)  # in case palindrome is even length

        return s[Solution.max_l:Solution.max_r + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome('cbabbak'))
