class Solution:
  isEven = False
  isOdd = False

  def leftEdgeM(self):
    if self.km >= 0:
      return self.M[self.km]
    else:
      return None
  
  def rightEdgeN(self):
    if (self.kn < 0):
      return self.N[0]
    else:
      if (self.kn == (self.n - 1)):
        return None
      return self.N[min(self.kn + 1, self.n - 1)]

  def rightEdgeM(self):
    if (self.km < 0):
      return self.M[0]
    else:
      if (self.km == (self.m - 1)):
        return None
      return self.M[min(self.km + 1, self.m - 1)]

  def isFinished(self):
    if self.isEven:
      if (self.km >= 0) and (self.kn >= 0):
        if (self.kn <= (self.n - 1)):
          leftEdgeN = self.N[self.kn]
          rEdgeN = self.rightEdgeN()
          rEdgeM = self.rightEdgeM()
          if (rEdgeM and rEdgeN):
            if ((self.M[self.km] <= self.N[self.kn + 1]) and (self.N[self.kn] <= self.M[self.km + 1])):
              return True
          else:
            if rEdgeM:
              if (self.N[self.kn] < rEdgeM):
                return True
              else:
                return False
            if rEdgeN:
              if (self.M[self.km] < rEdgeN):
                return True
              else: 
                return False
            
      if (self.km >= 0)  and (self.kn < 0):
        if ((self.M[self.km] <= self.N[0])):
          return True
      if ((self.km < 0) and (self.kn >= 0)):
        if (self.N[self.kn] <= self.M[0]):
          return True

    if self.isOdd:
      if ((self.km >= 0) and (self.kn >= 0)):
        rEdgeN = self.rightEdgeN()
        rEdgeM = self.rightEdgeM()
        if (rEdgeM and rEdgeN):
          if ((self.M[self.km] <= self.N[min(self.kn + 1, self.n-1)]) and (self.N[min(self.kn, self.n-1)] <= self.M[min(self.km + 1, self.m-1)])):
            return True
        else:
          return True
      if (self.km >= 0) and (self.kn < 0):
        if ((self.M[min(self.km, self.m-1)] <= self.N[0])):
          return True
      if ((self.km < 0) and (self.kn >= 0)):
        if (self.N[min(self.kn, self.n-1)] <= self.M[0]):
          return True
    return False

  def findMedianArray(self, A):
    if (len(A) % 2) == 1:
      return A[len(A) / 2]
    else: 
      p = len(A) / 2
      a = A[p - 1]
      b = A[p]
  
      return ((a + b )/ float(2)) 

  def findMedian(self):
    a = None
    b = None
    if self.isEven:
        if ((self.km >= 0) and(self.kn >= 0)):
          leftEdge = max(self.M[self.km], self.N[self.kn])
          if (self.km + 2 <= self.m):
            a = self.M[self.km + 1]
          else:
            a is None
          if (self.kn + 2 <= self.n):
            b = self.N[self.kn + 1]
          else:
            b is None

          if (a and b):
            rightEdge = min(a, b)
          if (b is None):
            rightEdge = a
          if (a is None):
            rightEdge = b

        if (self.km < 0):
          leftEdge = self.N[self.kn]
          if (self.rightEdgeN()):
            rightEdge = min(self.M[0], self.rightEdgeN())
          else:
            rightEdge = self.M[0]

        if (self.kn < 0):
          leftEdge = self.M[self.km]
          if (self.rightEdgeM()):
            rightEdge = min(self.N[0], self.rightEdgeM())
          else:
            rightEdge = self.N[0]


        leftEdge = float(leftEdge)
        rightEdge = float(rightEdge)
        return leftEdge + ((rightEdge - leftEdge) / float(2))
  
    if self.isOdd:
      if (self.km < 0):
        return max(self.N[min (self.kn + 1, self.n-1)], self.M[0])

      if (self.kn < 0):
        return min(self.M[self.km + 1], self.N[0])

      if ((self.km >= 0) and (self.kn >= 0)):
        if (self.km + 1 < self.m):
          edgeA = self.M[self.km + 1]
        else:
          return self.N[min(self.kn + 1, self.n - 1)]
        if (self.kn + 1 < self.n):
          edgeB = self.N[self.kn + 1]
        else:
          return self.M[self.km + 1]
        if (edgeA and edgeB):
          return min(edgeA, edgeB)
        
  def findMedianSortedArrays(self, A, B):
    lenA = len(A)
    lenB = len(B)
    if (lenB < 1):
      return self.findMedianArray(A)
    if (lenA < 1):
      return self.findMedianArray(B)
    if (lenA > lenB):
      self.m = lenA
      self.M = A
      self.n = lenB
      self.N = B
    else:
      self.m = lenB
      self.M = B
      self.n = lenA
      self.N = A

    if (((self.m+self.n)%2) == 1):
      self.isOdd = True
    else:
      self.isEven = True

    # k indicates the number of elements which should be found to the left AND right of the median
    self.k = (self.m + self.n) / 2
    diff = ((self.m - self.n) / 2) + ((self.m - self.n) % 2)
    # print "K is {}".format(self.k)
    if (self.isOdd):
      self.km = self.k - 1
    else:
      self.km = self.k - 1
    self.kn = -1 

    if(self.isFinished()):
      return self.findMedian()
    done = False
    self.kn = self.kn + 1
    self.km = self.km - 1
    prevpivot = -1
    LEFT = 0
    RIGHT = self.n - 1
    P = (RIGHT - LEFT) / 2
    M = LEFT + P
    while(not done):
      done = self.isFinished()
      if (not done):
        if (self.leftEdgeM() > self.rightEdgeN()):
          oldkn = self.kn
          LEFT = self.kn + 1
          P = (RIGHT - LEFT) / 2
          M = LEFT + P
          self.kn = M
          diff = self.kn - oldkn
          self.km = self.km - diff
        else:
          oldkn = self.kn
          RIGHT = self.kn - 1
          P = (RIGHT - LEFT) / 2
          M = LEFT + P
          self.kn = M
          diff = oldkn - self.kn
          self.km = self.km + diff
    return self.findMedian()