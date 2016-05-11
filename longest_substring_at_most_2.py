from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        letter_count = defaultdict(int)
        start = end = 0
        max_length = 0
        while end < len(s):
            letter_count[s[end]] += 1
            while len(letter_count) > 2:
                letter_count[s[start]] -= 1
                if letter_count[s[start]] == 0:
                    del letter_count[s[start]]
                start += 1
            end += 1
            max_length = max(max_length, end - start)
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringTwoDistinct('eceba'))
