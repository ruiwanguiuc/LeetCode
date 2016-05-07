class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        visited = {x: False for x in nums}
        maxl = 0
        for n in nums:
            if not visited[n]:
                visited[n] = True
                length = 1
                # explore right
                cur = n + 1
                while cur in visited:
                    visited[cur] = True
                    length += 1
                    cur += 1
                # explore left
                cur = n - 1
                while cur in visited:
                    visited[cur] = True
                    length += 1
                    cur -= 1
                maxl = max(maxl, length)
        return maxl


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
