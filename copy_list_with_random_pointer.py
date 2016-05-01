# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        old_to_new = {}
        if not head:
            return None
        newhead = RandomListNode(head.label)
        old_to_new[head] = newhead
        newcur = newhead
        cur = head.next
        while cur:
            newcur.next = RandomListNode(cur.label)
            newcur = newcur.next
            old_to_new[cur] = newcur
            cur = cur.next
        cur = head
        newcur = newhead
        while cur:
            newcur.random = old_to_new[cur.random] if cur.random else None
            cur = cur.next
            newcur = newcur.next
        return newhead
