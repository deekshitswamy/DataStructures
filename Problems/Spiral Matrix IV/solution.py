import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        pass

obj = Solution()
#data = obj.spiralMatrix(m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0])
data = obj.spiralMatrix(m = 1, n = 4, head = [0,1,2])
print(data)