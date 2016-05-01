# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # naive solution O(n). this doesn't use the property of BST
        # if not root:
        #     return None

        # def inorder(node):
        #     left = inorder(node.left) if node.left else []
        #     right = inorder(node.right) if node.right else []
        #     return left + [node] + right

        # l = inorder(root)
        # for i in range(len(l)):
        #     if l[i] == p:
        #         if i < len(l) - 1:
        #             return l[i + 1]
        #         else:
        #             return None

        # O(logn) https://leetcode.com/discuss/61105/java-python-solution-o-h-time-and-o-1-space-iterative
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ


if __name__ == "__main__":
    pass
