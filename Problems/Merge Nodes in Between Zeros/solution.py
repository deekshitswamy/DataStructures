import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        pass

obj = Solution()
#data = obj.mergeNodes(head = [0,3,1,0,4,5,2,0])
data = obj.mergeNodes(head = [0,1,0,3,0,2,2,0])
print(data)