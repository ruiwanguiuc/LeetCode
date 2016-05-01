# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        fast = slow = head
        prev_slow = None
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if not prev_slow:
            left = None
        else:
            prev_slow.next = None
            left = self.sortedListToBST(head)
        right = self.sortedListToBST(slow.next)
        root.left = left
        root.right = right
        return root
