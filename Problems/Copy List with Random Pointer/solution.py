import io

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        old_to_copy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            old_to_copy[cur]=copy
            cur=cur.next

        cur=head
        while cur:
            copy=old_to_copy[cur]
            copy.next=old_to_copy[cur.next]
            copy.random=old_to_copy[cur.random]
            cur=cur.next

        return old_to_copy[head]

obj = Solution()
#data = obj.copyRandomList(head = [[7,None],[13,0],[11,4],[10,2],[1,0]])
#data = obj.copyRandomList(head = [[1,1],[2,1]])
data = obj.copyRandomList(head = [[3,None],[3,0],[3,None]])
print(data)