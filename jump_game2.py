from collections import deque


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # jumps = [sys.maxint] * len(nums)
        # jumps[0] = 0
        # for i in range(len(nums)):
        #     for j in range(1, nums[i] + 1):
        #         dest = i + j
        #         if dest < len(nums):
        #             jumps[dest] = min(jumps[dest], jumps[i] + 1)
        # return jumps[-1]
        if not nums:
            return 0
        q = deque()
        q.append((0, 0))
        curmax = 0
        while q:
            cur, j = q.popleft()
            if cur == len(nums) - 1:
                return j
            if cur + nums[cur] >= len(nums) - 1:
                return j + 1
            for i in range(max(cur + 1, curmax), min(cur + nums[cur], len(nums) - 1) + 1):
                q.append((i, j + 1))
            curmax = max(curmax, cur + nums[cur])


if __name__ == "__main__":
    import ipdb; ipdb.set_trace()
    print Solution().jump([1, 2, 3])
