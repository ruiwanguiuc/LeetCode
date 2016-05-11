import sys


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_len = sys.maxint
        start = end = 0
        cur_sum = 0
        while end < len(nums):
            cur_sum += nums[end]
            while cur_sum >= s:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1
            end += 1
        return min_len if min_len != sys.maxint else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
