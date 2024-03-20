import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        t=0
        var=None
        while curr!=None:
            t+=1
            if t==b+1:
                break
            if a==t:
                pp=curr.next
                var=curr
                var.next=list2
                # curr.next=None
                curr=pp
            curr=curr.next
        temp=list1
        while temp!=None:
            if temp.next==None:
                break
            temp=temp.next
        temp.next=curr
        return list1


obj = Solution()
#data = obj.testfunc(list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002])
data = obj.testfunc(list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004])
print(data)