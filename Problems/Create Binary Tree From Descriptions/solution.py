import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> TreeNode:
        ans={}
        seen=set()
        for x,y,left in descriptions:
            if x not in ans:
                ans[x]=TreeNode(x)
            if y not in ans:
                ans[y]=TreeNode(y)
            if left:
                ans[x].left=ans[y]
            else:
                ans[x].right=ans[y]
            seen.add(y)
        for x,_,_ in descriptions:
            if x not in seen:
                return ans[x]

obj = Solution()
#data = obj.createBinaryTree(descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
data = obj.createBinaryTree(descriptions = [[1,2,1],[2,3,0],[3,4,1]])
print(data)