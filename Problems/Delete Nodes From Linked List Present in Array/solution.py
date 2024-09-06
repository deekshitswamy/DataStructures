import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: ListNode) -> ListNode:
        pass

obj = Solution()
#data = obj.modifiedList(nums = [1,2,3], head = [1,2,3,4,5])
#data = obj.modifiedList(nums = [1], head = [1,2,1,2,1,2])
data = obj.modifiedList(nums = [5], head = [1,2,3,4])
print(data)