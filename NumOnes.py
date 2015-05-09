import math
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        numones = 0
        if (n == 0):
            return 0
        numbits = int(math.ceil(math.log(n) / math.log(2)))
        for i in range(0, numbits + 1):
            pow = numbits - i 
            pow = math.pow(2, pow)
            if (n >= pow):
                numones = numones + 1
                n = n - pow
        return numones
        