class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
      if (not len(A)):
        return 0

      l = len(A)
      best = A[0]
      soFar = A[0]
      for i in range(1, l):
        now = A[i]
        soFar = soFar + now
        # print "At step {}, Best: {}, soFar: {}, now: {}".format(i, best, soFar, now)
        if (now > best):
          best = now
        if (soFar > best):
          best = soFar
        if (now > soFar):
          soFar = now
      return best

