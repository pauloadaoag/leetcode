class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if (x == 0):
            return 0
        if (x == 1):
            return 1
        g = 1.0
        for i in range(0, 20):
            g = (g + (x/g))/2
        return int(math.floor(g))