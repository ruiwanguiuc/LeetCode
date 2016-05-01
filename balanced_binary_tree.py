# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        result = self.helper(root)
        if result is False:
            return False
        else:
            return True

    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_height = self.helper(root.left) if root.left else 0
        right_height = self.helper(root.right) if root.right else 0
        if left_height is False or right_height is False:
            return False
        if abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height) + 1
