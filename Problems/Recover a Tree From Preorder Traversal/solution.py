import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        st = []
        i = 0
        while i < len(traversal):
            depth = 0
            while traversal[i] == '-':  
                depth += 1
                i += 1
            
            num = i
            while i < len(traversal) and traversal[i].isdigit():  
                i += 1
            val = int(traversal[num:i])  

            node = TreeNode(val)

            while st and st[-1][1] >= depth:
                st.pop()

            if st:
                parent = st[-1][0]
                if parent.left == None:
                    parent.left = node
                else:
                    parent.right = node
            
            st.append((node, depth))  

        return st[0][0]

obj = Solution()
#data = obj.recoverFromPreorder(traversal = "1-2--3--4-5--6--7")
#data = obj.recoverFromPreorder(traversal = "1-2--3---4-5--6---7")
data = obj.recoverFromPreorder(traversal = "1-401--349---90--88")
print(data)