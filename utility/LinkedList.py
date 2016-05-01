class LinkedList:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        if not self.next:
            return str(self.val) + "->None"
        return str(self.val) + "->" + str(self.next)

    def append(self, val):
        if not self.next:
            self.next = LinkedList(val)
        else:
            self.next.append(val)

    def find_mid(self):
        fast = self
        slow = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse(head):
        newhead = None
        while head:
            next = head.next
            head.next = newhead
            newhead = head
            head = next
        return newhead


if __name__ == "__main__":
    l = LinkedList(1)
    l.append(2)
    l.append(3)
    l.append(4)
    print str(l)
    print(l.find_mid())
    print(LinkedList.reverse(l))
