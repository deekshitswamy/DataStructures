import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        if head.val>4:
            head=ListNode(0,head)
        node=head
        while node:
            node.val=(node.val*2)%10
            if node.next and node.next.val>4:
                node.val+=1
            node=node.next
        return head

obj = Solution()
#data = obj.testfunc(n = 1)
#data = obj.testfunc(n = 2)
data = obj.testfunc(n = 2)
print(data)