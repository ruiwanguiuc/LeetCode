# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def serialize(self):
        left = self.left.serialize() if self.left else ['NULL']
        right = self.right.serialize() if self.right else ['NULL']
        return [self.val] + left + right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flatten_and_return(node):
            if not node:
                return None, None
            left_head, left_tail = flatten_and_return(node.left)
            right_head, right_tail = flatten_and_return(node.right)
            if left_head:
                node.right = left_head
                left_tail.right = right_head
                node.left = None
            else:
                node.right = right_head
            if right_tail:
                return node, right_tail
            elif left_tail:
                return node, left_tail
            else:
                return node, node
        if root:
            flatten_and_return(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(root.serialize())
    Solution().flatten(root)
    print(root.serialize())
