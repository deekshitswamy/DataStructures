import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize the matrix with -1
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        
        top, bottom, left, right = 0, m - 1, 0, n - 1
        curr = head
        
        # Traverse the matrix in spiral order
        while curr and top <= bottom and left <= right:
            # Fill top row (left to right)
            for i in range(left, right + 1):
                if curr:
                    ans[top][i] = curr.val
                    curr = curr.next
            top += 1
            
            # Fill right column (top to bottom)
            for i in range(top, bottom + 1):
                if curr:
                    ans[i][right] = curr.val
                    curr = curr.next
            right -= 1
            
            # Fill bottom row (right to left)
            for i in range(right, left - 1, -1):
                if curr:
                    ans[bottom][i] = curr.val
                    curr = curr.next
            bottom -= 1
            
            # Fill left column (bottom to top)
            for i in range(bottom, top - 1, -1):
                if curr:
                    ans[i][left] = curr.val
                    curr = curr.next
            left += 1
        
        return ans

obj = Solution()
#data = obj.spiralMatrix(m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0])
data = obj.spiralMatrix(m = 1, n = 4, head = [0,1,2])
print(data)