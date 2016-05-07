class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            bigger_than_left = mid == 0 or nums[mid] > nums[mid - 1]
            bigger_than_right = mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
            if bigger_than_left and bigger_than_right:
                return mid
            elif bigger_than_left and not bigger_than_right:
                left = mid + 1
            elif not bigger_than_left and bigger_than_right:
                right = mid - 1
            else:
                # going either way is ok since there are two peaks
                left = mid + 1
        return -1  # we shouldn't reach this line


if __name__ == "__main__":
    print(Solution().findPeakElement([1, 2, 3, 4, 5, 2, 1]))
