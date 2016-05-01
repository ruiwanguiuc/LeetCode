
class Solution(object):
    def balanced_parentheses(self, s):
        """
        Given a string with parentheses, return a string with balanced parentheses by
        removing the fewest characters possible. You cannot add anything to the string.

        NOTE: the difference between this and Leetcode remove invalid parentheses is here
        we can just return any of the result but Leetcode version we have to return all the
        valid results. And Leetcode version has chars other than ()

        Examples:

        balance("()") -> "()"
        balance(")(") -> ""
        balance("(((((") -> ""
        balance("(()()(") -> "()()"
        balance(")(())(") -> "(())"
        balance(")(())(") != "()()"
        """
        res = ''
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1
                res += c
            else:
                if right < left:
                    right += 1
                    res += c
        final_res = ''
        left = 0
        right = 0
        for c in reversed(res):
            if c == ')':
                right += 1
                final_res = c + final_res
            else:
                if left < right:
                    final_res = c + final_res
                    left += 1
        return final_res


if __name__ == "__main__":
    print(Solution().balanced_parentheses('()())()'))
    print(Solution().balanced_parentheses('((('))
    print(Solution().balanced_parentheses('(()()('))
    print(Solution().balanced_parentheses(')(())('))
