class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        b = s.rstrip().lstrip().split(' ')
        b = filter(lambda x: len(x) > 0, b)
        b.reverse()
        return ' '.join(b)