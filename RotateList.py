# https://oj.leetcode.com/problems/rotate-list/
# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
from utility.LinkedList import LinkedList
class RotateList:

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
	@staticmethod
	def rotate_list(head, k):
		return None


if __name__ == "__main__":
	l = LinkedList(1)
	l.append(2)
	l.append(3)
	l.append(4)
	l.append(5)
	print str(l)
	print str(RotateList.rotate_list(l, 2))