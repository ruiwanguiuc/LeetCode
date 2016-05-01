class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 4:
            return []
        ret = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r] + nums[i] + nums[j]
                    if s == target:
                        ret.add((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        return [list(r) for r in ret]


if __name__ == "__main__":
    pass
