# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def addTwoNumbers(l1, l2):
    ret = None
    cur = ret
    carry = 0
    while l1 and l2:
        val = (l1.val + l2.val) % 10 + carry
        carry = (l1.val + l2.val) / 10
        cur = ListNode(val)
        cur = cur.next
        l1 = l1.next
        l2 = l2.next
    if l1:
        cur = l1
    if l2:
        cur = l2
    return ret


if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(0)
    import ipdb; ipdb.set_trace()
    print(addTwoNumbers(l1, l2))
