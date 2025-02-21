import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.targets = set() #hashsets
        self.dfs(root, 0) #dfs search

    def find(self, target: int) -> bool:
        return target in self.targets #return target or else we return false
        
    def dfs(self, node, value): #dfs helper func
        if node is None: #none ie when we search for left and right but they don't do exist so we return none
            return
        self.targets.add(value) #if they exist, we add that value to the set
        self.dfs(node.left, value * 2 + 1) #recursive dfs search
        self.dfs(node.right, value * 2 + 2) #recovery operation for both
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)