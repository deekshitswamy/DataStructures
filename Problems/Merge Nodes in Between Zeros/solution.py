import io
from typing import List
from itertools import groupby
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        arr=[]
        cur=head
        while cur!=None:
            arr.append(cur.val)
            cur=cur.next
        newHead=ListNode(-1)
        cur=newHead
        for x,t in groupby(arr,key=lambda x: x==0):
            if not x:
                cur.next=ListNode(sum(t))  
                cur=cur.next
        return newHead.next

obj = Solution()
#data = obj.mergeNodes(head = [0,3,1,0,4,5,2,0])
data = obj.mergeNodes(head = [0,1,0,3,0,2,2,0])
print(data)