# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        cur = root  # current level
        prev = None  # the previous node in the next level
        head = None  # the head node in the next level

        while cur:
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left
                    if not head:
                        head = prev
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right
                    if not head:
                        head = prev
                cur = cur.next
            cur = head
            prev = None
            head = None


if __name__ == '__main__':
    print(Solution().connect(root))
