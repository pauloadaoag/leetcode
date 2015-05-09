class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
      if (not len(A)):
        return 0

      l = len(A)
      j = A.pop(0)
      best = j
      if (j < 0):
        soFar = 1
        mostNegative = j
      else:
        soFar = j
        mostNegative = 1
      
      for i in A:
        soFar = max(soFar, 1)
        # print ("Item: {} \tBest: {} \tSoFar: {} \tmostNegative: {}".format(i, best, soFar, mostNegative))
        if (i > best):
          best = i

        if (i == 0):
          soFar = 1
          mostNegative = 1
          best = max(best, 0)
          continue

        if (i > 0):
          soFar = soFar * i
          mostNegative = mostNegative * i
        if (i < 0):
          x = soFar
          soFar = mostNegative * i
          mostNegative = x * i

        best = max(best, soFar)

          # mostNegative = i
          # soFar = 1

      return best

