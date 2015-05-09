class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        output = []
        c = 1;
        while(len(digits) > 0):
            b = digits.pop()
            d = b + c
            e = 0
            if (d >= 10):
                c = 1
                e = d - 10
            else:
                c = 0
                e = d
            output.insert(0, e)
        if c == 1:
            output.insert(0, c)
        return output
