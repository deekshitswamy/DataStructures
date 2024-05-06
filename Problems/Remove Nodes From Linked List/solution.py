import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        cur=head
        temp=None
        #Reversing linkedlist
        while cur:
            cur.next,cur,temp=temp,cur.next,cur
        head=temp
        maxn=head.val
        prev=head
        cur=head.next
        #Checking maxn cur val is lesser than cur max or not
        while cur:
            if maxn>cur.val:
                maxn=max(maxn,cur.val)
                prev.next=cur.next
                cur=prev.next
            else:
                maxn=max(maxn,cur.val)
                prev=prev.next
                cur=cur.next
        cur=head
        temp=None
        #Reversing the linkedlist
        while cur:
            cur.next,cur,temp=temp,cur.next,cur
        return temp

obj = Solution()
#data = obj.removeNodes(head = [5,2,13,3,8])
data = obj.removeNodes(head = [1,1,1,1])
print(data)