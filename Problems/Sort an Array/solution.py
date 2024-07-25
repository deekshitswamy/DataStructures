import io
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapsize = len(nums)
        def heapify(idx: int): # tail recursion eliminated
            while True:
            # adjust into a heap assuming children are heaps
                left = idx * 2 + 1
                right = idx * 2 + 2
                maxi = nums[idx]
                maxiIdx = idx
                if left < heapsize and nums[left] > maxi:
                    maxi = nums[left]
                    maxiIdx = left
                if right < heapsize and nums[right] > maxi:
                    maxi = nums[right]
                    maxiIdx = right

                if maxiIdx == right: # pull up the new maximum
                    nums[idx], nums[right] = nums[right], nums[idx]
                    idx = right
                elif maxiIdx == left:
                    nums[idx], nums[left] = nums[left], nums[idx]
                    idx = left
                else: break
            
        for i in range(n-1, -1, -1): 
            heapify(i)

        # In-Place Heap Sort
        for i in range(n-1, -1, -1):
            # move max to the right
            nums[0], nums[i] = nums[i], nums[0]
            heapsize = i
            heapify(0)
        
        return nums

obj = Solution()
#data = obj.sortArray(nums = [5,2,3,1])
data = obj.sortArray(nums = [5,1,1,2,0,0])
print(data)