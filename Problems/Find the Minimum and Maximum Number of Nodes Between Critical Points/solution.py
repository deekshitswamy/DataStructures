import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        pass

obj = Solution()
#data = obj.nodesBetweenCriticalPoints(head = [3,1])
#data = obj.nodesBetweenCriticalPoints(head = [5,3,1,2,5,1,2])
data = obj.nodesBetweenCriticalPoints(head = [1,3,2,2,3,2,2,2,7])
print(data)