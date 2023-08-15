import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        pass

obj = Solution()
data = obj.partition(head = [1,4,3,2,5,2], x = 3)
#data = obj.partition(head = [2,1], x = 2)
print(data)