class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(ret)
            for j in range(len(ret) - l, len(ret)):
                ret.append(ret[j] + [nums[i]])
        return ret


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2, 3]))
