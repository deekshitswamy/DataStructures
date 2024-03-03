import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==0:
            return head
        fast=slow=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head

obj = Solution()
#data = obj.testfunc(n = 1)
#data = obj.testfunc(n = 2)
data = obj.testfunc(n = 2)
print(data)