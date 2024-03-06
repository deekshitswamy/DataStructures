import io
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True

        return False 

obj = Solution()
#data = obj.hasCycle(head = [3,2,0,-4], pos = 1)
#data = obj.hasCycle(head = [1,2], pos = 0)
data = obj.hasCycle(head = [1], pos = -1)
print(data)