import io
from functools import cache
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        pass

obj = Solution()
#data = obj.splitListToParts(head = [1,2,3], k = 5)
data = obj.splitListToParts(head = [1,2,3,4,5,6,7,8,9,10], k = 3)
print(data)