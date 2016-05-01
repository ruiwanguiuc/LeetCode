# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        l_paths = self.binaryTreePaths(root.left)
        r_paths = self.binaryTreePaths(root.right)
        all_paths = l_paths + r_paths
        if not all_paths:
            return [str(root.val)]
        return [
            str(root.val) + "->" + p
            for p in all_paths
        ]
