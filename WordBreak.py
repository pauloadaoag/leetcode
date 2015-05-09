class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    my_dict = None  
    cache = {}
    
    def wordBreak(self, s, dict):
        self.my_dict = dict
        self.cache = {}
        if (s in self.my_dict):
          return True
        return self.wordBreak_(s)


    def wordBreak_(self, s):
      if s in self.cache:
        return self.cache[s]
      if (s in self.my_dict):
          self.cache[s] = True
          return True
      l = len(s)
      for i in range(1,l):
        left = s[0:i]
        right = s[i:]
        if (left in self.my_dict):
          a =  self.wordBreak_(right)
          if a:
            self.cache[s] = True
            return True
      self.cache[s] = False
      return False



