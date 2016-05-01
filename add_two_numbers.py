# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return None
        p1 = l1
        p2 = l2
        s = p1.val + p2.val
        carry = s / 10
        ret = ListNode(s % 10)
        cur = ret
        p1 = p1.next
        p2 = p2.next
        while p1 and p2:
            s = p1.val + p2.val + carry
            carry = s / 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            s = p1.val + carry
            carry = s / 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            p1 = p1.next
        while p2:
            s = p2.val + carry
            carry = s / 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            p2 = p2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return ret


if __name__ == "__main__":
    pass
