class Solution:
    # @param A, a list of integers
    # @return an integer
    def computeTrap(self, seq, peak):
      l = len(seq)
      acc = 0
      for i in range(1, l - 1):
        if peak > seq[i]:
          acc = acc + (peak - seq[i])
      return acc


    def trap(self, A):
        deltas = [0]
        l = len(A)
        if l == 0: 
          return 0
        for i in range(1, l):
          deltas.append(A[i] - A[i-1])
        leftPeakIdx = 0
        leftPeak = A[0]
        rightPeak = 0
        rightPeakIdx = 0
        matched = False
        acc = 0
        while leftPeakIdx < l:
          leftPeak = A[leftPeakIdx]
          rightPeak = 0
          for i in range(leftPeakIdx + 1, l):
            if deltas[i] < 0:
              continue
            if deltas[i] == 0:
              if A[i] == leftPeak:
                leftPeak = A[i]
                leftPeakIdx = i
                rightPeak = 0
            if deltas[i] > 0:
              matched = True
              if A[i] >= leftPeak:
                rightPeak = A[i]
                rightPeakIdx = i
                acc = acc + self.computeTrap(A[leftPeakIdx:(rightPeakIdx + 1)], min(leftPeak, rightPeak))
                leftPeak = rightPeak
                leftPeakIdx = rightPeakIdx
                rightPeak = 0
              elif A[i] < leftPeak:
                if (A[i] > rightPeak):
                  rightPeak = A[i]
                  rightPeakIdx = i
                if i == (l - 1):
                  acc = acc + self.computeTrap(A[leftPeakIdx:(rightPeakIdx + 1)], min(leftPeak, rightPeak))
                  leftPeak = rightPeak
                  leftPeakIdx = rightPeakIdx
          if matched:
            matched = False
            acc = acc + self.computeTrap(A[leftPeakIdx:(rightPeakIdx + 1)], min(leftPeak, rightPeak))
            leftPeakIdx = rightPeakIdx
          else:
            leftPeakIdx = leftPeakIdx + 1
        return acc



          