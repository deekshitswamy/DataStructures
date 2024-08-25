import io
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def find(root, ans):
            if not root:
                return
            find(root.left, ans)
            find(root.right, ans)
            ans.append(root.val)
        
        ans = []
        find(root, ans)
        return ans

obj = Solution()
#data = obj.postorderTraversal(root = [1,None,2,3])
#data = obj.postorderTraversal(root = [])
data = obj.postorderTraversal(root = [1])
print(data)