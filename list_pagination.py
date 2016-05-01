from collections import deque


class Iter(object):

    def __init__(self, arr):
        self.i = 0
        self.arr = arr
        self.had_next = None

    def next(self):
        if not self.has_next():
            raise StopIteration
        ret = self.arr[self.i]
        self.i += 1
        self.had_next = True
        return ret

    def has_next(self):
        return self.i < len(self.arr)

    def remove(self):
        if not self.had_next:
            raise Exception
        del self.arr[self.i - 1]
        self.i -= 1
        self.had_next = False


def list_pagination(arr, num):
    page = 0
    hosts_this_page = set()
    count = 0
    while arr:
        print('PAGE: ' + str(page))
        it = Iter(arr)
        while it.has_next():
            cur = it.next()
            if cur not in hosts_this_page:
                print(cur)
                count += 1
                hosts_this_page.add(cur)
                it.remove()
                if count == num:
                    break
        hosts_this_page.clear()
        count = 0
        page += 1


if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2, 1, 1, 4, 5]
    list_pagination(arr, 3)
