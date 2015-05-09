class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    digits = set(['1','2','3','4','5','6','7','8','9'])
    minedge  = {
        0: 0,
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 3,
        6: 6,
        7: 6,
        8: 6
    }

    maxedge = {
        0:2,
        1:2,
        2:2,
        3:5,
        4:5,
        5:5,
        6:8,
        7:8,
        8:8
    }

    board = []

    def getCandidates(self, pos):
        # return candidate values
        a = self.getCandidatesX(pos)
        # #print a
        b = self.getCandidatesY(pos)
        # #print b
        c = self.getCandidatesSquare(pos)
        # #print c
        sol = a.intersection(b)
        sol = sol.intersection(c)
        return sol

    def getCandidatesX(self, pos):
        #return candidates
        tagged = [w for w in self.board[pos['y']] if w != '.']
        # #print tagged
        return self.digits.difference(set(tagged))

    def getCandidatesY(self, pos):
        #return candidates down line
        tagged = [w[pos['x']] for w in self.board if w[pos['x']] != '.']
        return self.digits.difference(set(tagged))

    def getCandidatesSquare(self, pos):
        #return candidates in square
        mylist = []
        for x in range(self.minedge[pos['x']], self.maxedge[pos['x']] + 1):
            for y in range(self.minedge[pos['y']], self.maxedge[pos['y']] + 1):
                if self.board[y][x] != '.':
                    mylist.append(self.board[y][x])
        return self.digits.difference(set(mylist))

    def getNextCandidate(self, pos):
        for y in range(pos['y'], 9):
            if (y == pos['y']):
                for x in range(pos['x'] + 1, 9):
                    if self.board[y][x] == '.':
                        return {'x':x, 'y':y}
            else:
                for x in range(0, 9):
                    if self.board[y][x] == '.':
                        return {'x':x, 'y':y}
        return None


    def solveSudoku(self, board_):
        self.board = board_;
        positions = [] #stack for positions
        if (self.board[0][0]) == '.':
            pos = {'x' : 0, 'y': 0}
        else: 
            pos = self.getNextCandidate({'x':0, 'y':0})
        self.solveSudoku_(pos)

    def solveSudoku_(self, pos):
        candidates = self.getCandidates(pos)
        if (len(candidates) == 0):
            return
        nextpos = self.getNextCandidate(pos)
        
        for candidate in candidates:
            temp = list(self.board[pos['y']])
            temp[pos['x']] = candidate
            self.board[pos['y']]  =  "".join(temp)  
            if (nextpos):
                a = self.solveSudoku_(nextpos)
                if (a is True):
                    return True
                else:
                    temp = list(self.board[pos['y']])
                    temp[pos['x']] = '.'
                    self.board[pos['y']]  =  "".join(temp)
        if (nextpos is None):
            return True
