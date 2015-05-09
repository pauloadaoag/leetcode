class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if ((m == 0) or (n == 0)):
          return 0
        if (n > m):
          return self.uniquePaths(n, m)
        
        row = [1] * m

        for i in range(1, n):
          # print row
          r2 = [1]
          last = 1
          for j in range(1, m):
            last = last + row[j]
            r2.append(last)
          row = r2
        return row.pop()
