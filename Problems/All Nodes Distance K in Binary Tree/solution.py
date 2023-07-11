import io
from typing import List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=[root]
        d=defaultdict(list)#store neighbours
        while(q):
            
            for i in range(len(q)):
                x=q.pop(0)
                if x.left:
                    d[x].append(x.left)
                    d[x.left].append(x)
                    q.append(x.left)
                if x.right:
                    d[x.right].append(x)
                    d[x].append(x.right)
                    q.append(x.right)


        #find the nodes at distance k
        q=[target]
        vis=set()
        vis.add(target)
        while(q and k>0):
            
            for i in range(len(q)):
                x=q.pop(0)
                for node in d[x]:
                    if node not in vis:
                        vis.add(node)
                        q.append(node)
            k-=1 
        ans=[]
        
        for node in q:
            ans.append(node.val)
        return ans

# example 1
# node1 = TreeNode(val=7,left=None, right=None)
# node2 = TreeNode(val=15,left=None, right=None)
# node3 = TreeNode(val=9,left=None, right=None)
# node4 = TreeNode(val=20,left=node2, right=node1)
# root = TreeNode(val=3,left=node3, right=node4)

#example 2
node1 = TreeNode(val=6,left=None, right=None)
node2 = TreeNode(val=5,left=None, right=node1)
node3 = TreeNode(val=4,left=None, right=node2)
node4 = TreeNode(val=3,left=None, right=node3)
root = TreeNode(val=2,left=None, right=node4)

obj = Solution()
data = obj.distanceK(root)
print(data)