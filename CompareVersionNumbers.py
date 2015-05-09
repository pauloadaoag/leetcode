class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1_ = version1.split(".")
        v2_ = version2.split(".")
        v1_.reverse()
        v2_.reverse()
        v1 = []
        v2 = []
        start = False
        for x in v1_:
            if int(x) != 0:
                start = True
            if start:
                v1.append(x)
        start = False
        for x in v2_:
            if int(x) != 0:
                start = True
            if start:
                v2.append(x)
        v1.reverse()
        v2.reverse()
        l = min(len(v1), len(v2))
        for x in range(0, l):
            v1_digit = int(v1[x])
            v2_digit = int(v2[x])
            if (v1_digit > v2_digit):
                return 1
            if (v1_digit < v2_digit):
                return -1
                
        if (len(v1) > len(v2)):
            return 1
        if (len(v2) > len(v1)):
            return -1
        return 0
