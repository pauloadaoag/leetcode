# #1 - Two SUm
class Solution:
  def binarySearch(self,num, target):
    l = len(num)
    p = l/2
    pivot = l - p
    oldp = l
    while (pivot > 0):
      if num[p] == target:
        return p
      if num[p] < target:
        pivot = pivot / 2
        p = p + pivot
      if num[p] > target:
        pivot = pivot / 2
        p = p - pivot
    return -1


  def find(self, numbers, target):
    num = sorted(numbers)
    l = len(num)
    l2 = l - 1
    for i in range(0, l):
      a1 = num[i]
      jstart = i + 1
      t = target - a1
      if (t == a1):
        if (num.count(target) == 1):
          continue
      idx = self.binarySearch(num, t)
      if idx != -1:
        return (a1, t)

  def twoSum(self, num, target): 
    soln = self.find(num, target)
    a1 = num.index(soln[0])
    del num[a1]
    a2 = num.index(soln[1])
    if (a2 >= a1):
      a2 = a2 + 1
    if (a2 < a1):
      a2 = a2
    indices = [a1 + 1, a2 + 1]
    return (min(indices), max(indices))