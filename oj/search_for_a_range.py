class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        first = last = -1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                first_index = self.firstIndex(nums, target, l, mid - 1)
                last_index = self.lastIndex(nums, target, mid + 1, r)
                if first_index == -1:
                    first = mid
                else:
                    first = first_index
                if last_index == -1:
                    last = mid
                else:
                    last = last_index
                return [first, last]
        return [first, last]
                
                
                
    def firstIndex(self, nums, target, l, r):
        first_index = -1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                first_index = mid
                r = mid - 1
        return first_index
        
    def lastIndex(self, nums, target, l, r):
        last_index = -1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                last_index = mid
                l = mid + 1
        return last_index
        

if __name__ == "__main__":
    print(Solution().searchRange([1], 1))
        