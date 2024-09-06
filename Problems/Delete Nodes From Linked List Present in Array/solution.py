import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: ListNode) -> ListNode:
        hashSet = set()

        for num in nums:
            hashSet.add(num)

        ptr = head
        while ptr.next:
            if ptr.next.val in hashSet:
                ptr.next = ptr.next.next
            else: ptr = ptr.next

        if head.val in hashSet:
            head = head.next

        return head

obj = Solution()
#data = obj.modifiedList(nums = [1,2,3], head = [1,2,3,4,5])
#data = obj.modifiedList(nums = [1], head = [1,2,1,2,1,2])
data = obj.modifiedList(nums = [5], head = [1,2,3,4])
print(data)