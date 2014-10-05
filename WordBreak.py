# source of this problem:
# http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
class WordBreak:

	@staticmethod
	def word_break(word_to_break, word_set):
		if not word_to_break:
			return ""
		if word_to_break in word_set:
			return word_to_break
		for i in range(len(word_to_break)):
			first_half = word_to_break[:i+1]
			if first_half in word_set:
				remaining = word_to_break[i+1:]
				remaining_word_segment = WordBreak.word_break(remaining, word_set)
				if remaining_word_segment:
					return first_half + " " + remaining_word_segment
		return ""

if __name__ == "__main__":
	print WordBreak.word_break('applepie', set(['apple', 'pie', 'app', 'person']))