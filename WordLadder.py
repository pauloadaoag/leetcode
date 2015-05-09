# #127 - Word Ladder
from pprint import pprint
import collections

class Solution:
  def ladderLength(self, start, end, dict):
    dict.append(end)
    wordLen = len(start)
    #Create double ended queue
    queue = collections.deque([(start, 1)])
    while queue:
      curr = queue.popleft()
      currWord = curr[0]
      currLen = curr[1]
      if currWord == end:
        return currLen
      for i in xrange(wordLen):
        part1 = currWord[:i]
        part2 = currWord[i+1:]
        for j in 'abcdefghijklmnopqrstuvwxyz':
          if currWord[i] != j:
            nextWord = part1 + j + part2
            if nextWord in dict:
              queue.append((nextWord, currLen + 1))
              dict.remove(nextWord)
    return 0
