class Solution:
    # @return an integer
    vals = {}
    vals[0] = 1;
    vals[1] = 1;
    vals[2] = 2;
    vals[3] = 5;
    def numTrees(self, n):
        if (n in self.vals):
            return self.vals[n]
        else:
            acc = 0;
            acc = acc + 2* self.numTrees(n-1)
            for i in range(1, (n-1)):
                j = n - i - 1;
                acc = acc + (self.numTrees(j) * self.numTrees(i))
            self.vals[n] = acc
            return acc