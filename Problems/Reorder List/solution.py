import io
from typing import List
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        q=deque()
        p=head.next
        while p:
            q.append(p)
            p=p.next
        p=head
        while len(q):
            p.next=q.pop()
            p=p.next
            if len(q):
                p.next=q.popleft()
                p=p.next
        p.next=None

obj = Solution()
#data = obj.reorderList(head = [1,2,3,4])
data = obj.reorderList(head = [1,2,3,4,5])
print(data)