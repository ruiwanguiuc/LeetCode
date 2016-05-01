class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sums = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                twosum = nums[l] + nums[r]
                if twosum == target:
                    sums.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif twosum > target:
                    r -= 1
                else:
                    l += 1
        return sums


if __name__ == "__main__":
    pass
