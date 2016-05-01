
class Solution(object):
    def num_spaces_evenly(self, total_spaces, num_slots):
        """
        divide spaces with a total count into multiple slots evenly.
        the empty slots on the left will be assigned more spaces than
        the slots on the right.

        e.g.
        total_spaces: 16, num_slots: 2 -> [8, 8]
        total_spaces: 3, num_slots: 2 -> [2, 1]
        """
        base_n_spaces = total_spaces / num_slots
        reminder = total_spaces - base_n_spaces * num_slots
        ret = [base_n_spaces] * num_slots
        for i in range(reminder):
            ret[i] += 1
        return ret

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        i = 0
        lines = []
        while i < len(words):
            # get as many words as possible for this line
            # put first word in since there is at least one word for this line
            cur_l = len(words[i])
            cur_start = i
            n_spaces = maxWidth - cur_l
            i += 1
            while i < len(words):
                next_l = cur_l + len(words[i]) + 1
                if next_l > maxWidth:
                    break
                cur_l = next_l
                n_spaces -= len(words[i])
                i += 1

            # format this line. all the words for this line are words[cur_start:i]
            num_words = i - cur_start
            # corner case 1: there is only 1 word in this line
            if num_words == 1:
                lines.append(words[cur_start] + ' ' * n_spaces)
            # corner case 2: this is the last line. It should be left justified and
            # no extra space is inserted between words.
            elif i == len(words):
                line = ' '.join(words[cur_start:])
                line += ' ' * (maxWidth - len(line))
                lines.append(line)
            else:
                spaces = self.num_spaces_evenly(n_spaces, num_words - 1)
                line = words[cur_start]
                for w, spaces in zip(words[cur_start + 1:i], spaces):
                    line += ' ' * spaces + w
                lines.append(line)
        return lines


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print Solution().fullJustify(words, maxWidth)
