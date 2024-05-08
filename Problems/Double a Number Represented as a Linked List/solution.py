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
#data = obj.doubleIt(head = [1,8,9])
data = obj.doubleIt(head = [9,9,9])
print(data)