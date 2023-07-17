import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        while l1 is not None:
            num1 = l1.val + (num1*10)
            l1 = l1.next
        while l2 is not None:
            num2 = l2.val + (num2*10)
            l2= l2.next
        
        sumlink = self.createLinkedList(list(str(num1+num2)))
        return sumlink

    def createLinkedList(self, digits: List) -> ListNode:
        headnode = ListNode()
        prevnode = ListNode()
        first = True
        for d in digits:
            if first:
                headnode.val = d
                prevnode = headnode
                first = False
                continue
            node = ListNode()
            node.val = d
            prevnode.next = node
            prevnode = node    
        return headnode

    def LinkedListToList(self, sumlink: ListNode) -> List:
        numlist = list()
        while sumlink is not None:
            numlist.append(int(sumlink.val))
            sumlink = sumlink.next
        return numlist


obj = Solution()
# example 1
#l1 = [7,2,4,3], l2 = [5,6,4]
l1 = obj.createLinkedList(digits = [7,2,4,3])
l2 = obj.createLinkedList(digits = [5,6,4])

# example 2 
# l1 = [2,4,3], l2 = [5,6,4]
# l1 = obj.createLinkedList(digits = [2,4,3])
# l2 = obj.createLinkedList(digits = [5,6,4])

# example 3
# l1 = [0], l2 = [0]
# l1 = obj.createLinkedList(digits = [0])
# l2 = obj.createLinkedList(digits = [0])

sumlink = obj.addTwoNumbers(l1, l2)
data = obj.LinkedListToList(sumlink)
print(data)