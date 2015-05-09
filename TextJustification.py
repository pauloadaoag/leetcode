class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    
    def spaces(self, num):
        return ' '*num
        
    def fullJustify(self, words, L):
        line = []
        output = []
        linelength = 0
        if (len(words) == 0):
            return [""]
        if (L == 0):
            return [""]
        for word in words:
            wordlength = len(word)
            if (linelength + wordlength + (len(line) - 1)) < L:
                line.append(word)
                linelength = linelength + wordlength
            else:
                numspaces = L - linelength
                wordcnt  = len(line)
                if (wordcnt == 1):
                    outputline = line[0] + (self.spaces(numspaces))
                    output.append(outputline)
                else:
                    spaces = numspaces/(wordcnt - 1)
                    rem_spaces = numspaces % (wordcnt - 1)
                    for j in range(0, rem_spaces):
                        line[j] = line[j] + " "
                    seed = self.spaces(spaces)
                    outputline = seed.join(line)
                    output.append(outputline)
                line = [word]
                linelength = len(word)
        numspaces = L - linelength
        wordcnt  = len(line)
        if (wordcnt == 1):
            # print wordcnt
            # print numspaces
            outputline = line[0] + (self.spaces(numspaces))
            output.append(outputline)
        else:
            spaces = numspaces/(wordcnt - 1)
            #rem_spaces = numspaces % (wordcnt - 1)
            #for j in range(0, rem_spaces):
            #    line[j] = line[j] + " "
            #seed = self.spaces(spaces)
            seed = " "
            outputline = seed.join(line)
            outputline = outputline + self.spaces(L - len(outputline))
            output.append(outputline)
        oput = [o for o in output if len(o) > 0]
        return oput