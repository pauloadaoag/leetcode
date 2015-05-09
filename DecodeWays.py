class Solution:
    # @param s, a string
    # @return an integer
    def countRecursive(self,idx, s):
      if (idx >= len(s)):
        return 0
      c = s[idx]
      if (c in '3456789'):
        return 1
      if (c in '12'):
        return 1 + self.countRecursive(idx + 1, s)
      if (c in '0'):
        return 0

    def numDecodings(self, s):
      return self.countRecursive(0, s)