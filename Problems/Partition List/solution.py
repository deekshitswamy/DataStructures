import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> [ListNode]:
        slist, blist = ListNode(), ListNode()
        small, big = slist, blist # dummy lists

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = blist.next
        big.next = None # prevent linked list circle

        return slist.next


node5 = ListNode(2, None)
node4 = ListNode(5, node5)
node3 = ListNode(2, node4)
node2 = ListNode(3, node3)
node1 = ListNode(4, node2)
root = ListNode(1, node1)

# example 2
# node1 = ListNode(1, None)
# root = ListNode(2, node1)

obj = Solution()
data = obj.partition(head = root, x = 3)
#data = obj.partition(head = root, x = 2)
ans = []
while data:
    ans.append(data.val)
    data = data.next
print(ans)