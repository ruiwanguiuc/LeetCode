# ref: http://www.cnblogs.com/zuoyuan/p/3780167.html


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        k = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break
        if k == -1:
            nums.reverse()
            return
        l = -1
        for i in range(len(nums) - 1, i, -1):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = nums[k + 1:][::-1]
