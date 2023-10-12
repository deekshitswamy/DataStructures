import io
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        pass

obj = Solution()
#data = obj.findInMountainArray(array = [1,2,3,4,5,3,1], target = 3)
data = obj.findInMountainArray(array = [0,1,2,4,2,1], target = 3)
print(data)