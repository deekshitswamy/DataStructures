import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level=0
        curlevel=[root]
        nextlevel=[]
        while curlevel:
            for i in range(len(curlevel)):
                curr=curlevel[i]
                if curr.left:
                    nextlevel.append(curr.left)
                if curr.right:
                    nextlevel.append(curr.right)
                if curr.val%2==level%2:
                    return False
                if i>0 and level%2==0 and curr.val<=curlevel[i-1].val:
                    return False
                if i>0 and level%2!=0 and curr.val>=curlevel[i-1].val:
                    return False
            curlevel=nextlevel
            nextlevel=[]
            level+=1                        
        return True

obj = Solution()
#data = obj.isEvenOddTree(root = [1,10,4,3,null,7,9,12,8,6,null,null,2])
#data = obj.isEvenOddTree(root = [5,4,2,3,3,7])
data = obj.isEvenOddTree(root = [5,9,1,3,5,7])
print(data)