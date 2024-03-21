import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            prev,head.next,head=head,prev,head.next
        return prev

obj = Solution()
#data = obj.reverseList(head = [1,2,3,4,5])
#data = obj.reverseList(head = [1,2])
data = obj.reverseList(head = [])
print(data)