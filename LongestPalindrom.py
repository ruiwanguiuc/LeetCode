# https://oj.leetcode.com/problems/longest-palindromic-substring/

# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, and 
# there exists one unique longest palindromic substring.
class LongestPalindrom:

	@staticmethod
	def find_longest_palindrom(s):
		longest_p = ""
		length_longest = 0
		for i in range(len(s)):
			longest_p, length_longest = expand(i, i, s, length_longest, longest_p)
			longest_p, length_longest = expand(i, i+1, s, length_longest, longest_p)
		return longest_p

def expand(left, right, s, length_longest, longest_p):
	"""expands the string from left/right index until it is not palindromic
	update length_longest and longest_p if necessary and return them.
	"""
	length_p = right - left - 1
	while left >= 0 and right < len(s):
		if s[left] != s[right]:
			break
		left -= 1
		right += 1
		length_p += 2
	if length_p > length_longest:
		return s[left+1:right], length_p
	else:
		return longest_p, length_longest


if __name__ == "__main__":
	print LongestPalindrom.find_longest_palindrom('thisisatest')
	print LongestPalindrom.find_longest_palindrom('trickyykabakyi')