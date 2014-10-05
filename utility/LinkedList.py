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


if __name__ == "__main__":
	l = LinkedList(1)
	l.append(2)
	l.append(3)
	print str(l)

