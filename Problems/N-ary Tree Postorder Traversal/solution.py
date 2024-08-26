import io
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.result = []

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return self.result
        
        for child in root.children:
            self.postorder(child)
        self.result.append(root.val)
        
        return self.result

obj = Solution()
#data = obj.postorder(root = [1,None,3,2,4,None,5,6])
data = obj.postorder(root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
print(data)