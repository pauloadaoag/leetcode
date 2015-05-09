# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        curnode1 = l1
        curnode2 = l2
        
        a = None
        edgenode = None
        carry = 0
        if (curnode1 is None):
            return None
        while(curnode1 or curnode2):
            v1 = 0
            v2 = 0
            if (curnode1):
                v1 = curnode1.val
            if (curnode2):
                v2 = curnode2.val
            
            total = v1 + v2 + carry
            if (total >= 10):
                carry = 1
                total = total - 10
            else:
                carry = 0
            if (edgenode is None):
                a = ListNode(total)
                edgenode = a
            else:
                b = ListNode(total)
                edgenode.next = b
                edgenode = b
            if (curnode1):
                curnode1 = curnode1.next
            if (curnode2):
                curnode2 = curnode2.next
        if (carry > 0):
            b = ListNode(1)
            edgenode.next = b
        return a
            