import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        pass

obj = Solution()
#data = obj.removeZeroSumSublists(head = [1,2,-3,3,1])
#data = obj.removeZeroSumSublists(head = [1,2,3,-3,4])
data = obj.removeZeroSumSublists(head = [1,2,3,-3,-2])
print(data)