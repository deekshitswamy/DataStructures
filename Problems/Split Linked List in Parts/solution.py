import io
from functools import cache
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        ans=[]
        cur=head
        n=0
        while cur:
            n+=1
            cur=cur.next

        part,left=n//k,n%k
        cur=head
        prev=None
        for i in range(k):
            ans.append(cur)
            for _ in range(part):
                if cur:
                    prev=cur
                    cur=cur.next

            if left and cur:
                prev=cur
                cur=cur.next
                left-=1

            if prev:
                prev.next=None

        return ans

obj = Solution()
#data = obj.splitListToParts(head = [1,2,3], k = 5)
data = obj.splitListToParts(head = [1,2,3,4,5,6,7,8,9,10], k = 3)
print(data)