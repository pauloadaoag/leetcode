class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        permutations = []
        #print "\npermuting!"
        #print num
        l = len(num)
        if (l == 0):
            return []
        if (l == 1):
            return [num]
        for i in range(0, l):
            localp = []
            tnum = num[:]

            a = tnum.pop(i)
            #print "tnum"
            #print tnum
            #print num
            localp = self.permute(tnum)
            #print "localp"
            #print localp
            for p in localp:
                p.insert(0, a)
            permutations = permutations + localp
        return permutations

