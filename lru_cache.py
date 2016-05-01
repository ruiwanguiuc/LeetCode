class ListNode(object):
    """
    Doubly linked list. The head will be the least recently used element
    and the tail will be the most recently used element.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.map = {}
        self.head = None
        self.tail = None

    def remove_head(self):
        """
        Remove self.head, update self.head and return the old head node
        """
        ret = self.head
        self.head = self.head.next
        self.head.prev = None
        return ret

    def append_tail(self, key, val):
        """
        Append a ListNode to the tail of the linked list and update self.tail
        (assuming self.tail is not None)
        """
        cur = ListNode(key, val)
        self.tail.next = cur
        cur.prev = self.tail
        self.tail = cur

    def update(self, key, value):
        """
        Update the ListNode of iput key value. This is the method we want to call
        after we "used" this key. (either get or set)
        i.e. move this ListNode to self.tail and adjust the whole list accordingly
        """
        cur = self.map[key]
        cur.val = value
        # if this is already the tail then we don't need to do anything
        if cur != self.tail:
            self.append_tail(key, value)
            if cur == self.head:
                self.map[key] = self.tail
                self.remove_head()
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            self.map[key] = self.tail

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.map:
            return -1
        cur = self.map[key]
        self.update(key, cur.val)
        return cur.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.head:
            self.head = ListNode(key, value)
            self.tail = self.head
            self.map[key] = self.head
            self.size = 1
        else:
            if key not in self.map:
                self.append_tail(key, value)
                self.map[key] = self.tail
                self.size += 1
                if self.size > self.cap:
                    removed = self.remove_head()
                    del self.map[removed.key]
            else:
                self.update(key, value)


if __name__ == "__main__":
    pass
