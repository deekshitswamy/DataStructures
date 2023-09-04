import io

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        pass

obj = Solution()
#data = obj.hasCycle(head = [3,2,0,-4], pos = 1)
#data = obj.hasCycle(head = [1,2], pos = 0)
data = obj.hasCycle(head = [1], pos = -1)
print(data)