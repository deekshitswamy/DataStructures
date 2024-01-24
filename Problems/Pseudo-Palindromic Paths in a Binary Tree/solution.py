import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans=0
        def search(node,even):
            if node==None:
                return
            even[node.val]= not even[node.val]
            if node.left==None and node.right==None:
                if sum(even)<=1:
                    nonlocal ans
                    ans+=1
            else:
                search(node.left,even)
                search(node.right,even)
            even[node.val]= not even[node.val]
        search(root,[False]*10)
        return ans

obj = Solution()
#data = obj.pseudoPalindromicPaths(root = [2,3,1,3,1,null,1])
#data = obj.pseudoPalindromicPaths(root = [2,1,1,1,3,null,null,null,null,null,1])
data = obj.pseudoPalindromicPaths(root = [9])
print(data)