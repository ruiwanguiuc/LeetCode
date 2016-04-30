class Node:
    def __init__(self, val):
        self.val = val
        self.lcount = 0  # how many nodes are there in the left subtree
        self.dup = 1  # how many duplicate vals have we seen
        self.left = None
        self.right = None

    def insert_and_count(self, val):
        cur = self
        total_count = 0
        while cur:
            if val == cur.val:
                cur.dup += 1
                return total_count + cur.lcount
            elif val < cur.val:
                cur.lcount += 1
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    return total_count
            else:
                total_count += (cur.dup + cur.lcount)
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    return total_count


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # naive O(n^2) solution
        #
        # counts = [0] * len(nums)
        # for i in range(len(nums)):
        #     c = 0
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             c += 1
        #     counts[i] = c
        # return counts

        # O(n log n) using BST
        if not nums:
            return []
        root = Node(nums[-1])
        counts = [0]
        for n in reversed(nums[:-1]):
            # import ipdb;ipdb.set_trace()
            count = root.insert_and_count(n)
            counts.append(count)
        return list(reversed(counts))


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))
