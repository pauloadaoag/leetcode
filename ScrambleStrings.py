class Solution:
  # @return a boolean
  def is_anagram(self, s1, s2):
    return (sorted(s1) == sorted(s2))

  def isScramble(self, s1, s2):
    if (len(s1) != len(s2)):
      return False
    if (len(s1) < 1):
      return True
    if (s1 == s2):
      return True

    return self.isScramble_(s1, s2)

  def isScramble_(self, s1, s2):
    l = len(s1)
    if l == 1:
      if s1 == s2:
        return True
      else:
        return False

    for mp in range(1, l):

      left1 = s1[0:mp]
      right1 = s1[mp:]

      left2 = s2[0:mp]
      right2 = s2[mp:]

      diff = l - mp
      aleft2 = s2[0:diff]
      aright2 = s2[diff:]


      llen = len(left1)
      rlen = len(right1)

      solFound = False
      # if (rlen == llen):
      if (self.is_anagram(left1, left2) and self.is_anagram(right1, right2)):
        temp1 = (self.isScramble_(left1, left2)  )
        temp2 =  self.isScramble_(right1, right2)
        solFound = solFound or (temp1 and temp2)
      elif (self.is_anagram(left1, right2) and self.is_anagram(left2, right1)):
        temp1 = (self.isScramble_(left1, right2)  )
        temp2 =  self.isScramble_(left2, right1)
        solFound = solFound or (temp1 and temp2) 
      elif (self.is_anagram(left1, aright2) and self.is_anagram(right1, aleft2)):
        temp1 = (self.isScramble_(left1, aright2)  )
        temp2 =  self.isScramble_(right1, aleft2)
        solFound = solFound or (temp1 and temp2)     
      else:
        solFound = solFound or False

      
      if solFound is True:
        return True

    return False
  