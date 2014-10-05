class WordBreak:

	@staticmethod
	def word_break(word_to_break, word_set):
		if not word_to_break:
			return ""
		for i in range(len(word_to_break)):
			if word_to_break[:i+1] in word_set:
				
		return word_to_break

if __name__ == "__main__":
	print WordBreak.word_break('applepie', set(['apple', 'pie', 'and', 'person']))