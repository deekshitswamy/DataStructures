import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        positions = {x: i for i, x in enumerate(postorder)}
        st: List[TreeNode] = []
        for x in preorder:
            cur = TreeNode(x)
            while st and positions[st[-1].val] < positions[x]:
                st.pop()
            if st:
                if st[-1].left is None:
                    st[-1].left = cur
                else:
                    st[-1].right = cur
            st.append(cur)
        return st[0]

obj = Solution()
#data = obj.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])
data = obj.constructFromPrePost(preorder = [1], postorder = [1])
print(data)