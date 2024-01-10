import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        graph=defaultdict(list)
        stack=[(root,None)]
        while stack:
            n,p=stack.pop()
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)
            if n.left:
                stack.append((n.left,n))
            if n.right:
                stack.append((n.right,n))
        ans=-1
        seen={start}
        queue=deque([start])
        while queue:
            for _ in range(len(queue)):
                u=queue.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            ans+=1
        return ans 

obj = Solution()
#data = obj.amountOfTime(root = [1], start = 1)
data = obj.amountOfTime(root = [1,5,3,None,4,10,6,9,2], start = 3)
print(data)