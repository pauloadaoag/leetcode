class Solution:
    # @param n, an integer
    # @return an integer
    cache = {
            1:1
        }
    def climbStairs(self, n):
        if n <= 1:
            return 1
        if (self.cache.has_key(n)):
            return self.cache[n]
        else:
            a = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = a
            return a