import io

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        pass

obj = Solution()
#data = obj.copyRandomList(head = [[7,None],[13,0],[11,4],[10,2],[1,0]])
#data = obj.copyRandomList(head = [[1,1],[2,1]])
data = obj.copyRandomList(head = [[3,None],[3,0],[3,None]])
print(data)