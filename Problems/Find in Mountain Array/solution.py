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
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        low=0
        high=n-1
        max_index=0
        while low<high:
            mid=low+(high-low)//2
            if mountain_arr.get(mid)>mountain_arr.get(mid+1):
                high=mid
            else:
                low=mid+1
        max_index=low
        low=0
        high=max_index

        while low<=high:
            mid=low+(high-low)//2
            midarr=mountain_arr.get(mid)
            if midarr<target:
                low=mid+1
            elif midarr>target:
                high=mid-1
            else:
                return mid

        low=max_index
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            midarr=mountain_arr.get(mid)
            if midarr>target:
                low=mid+1
            elif midarr<target:
                high=mid-1

            else:
                return mid
        return -1                                            

obj = Solution()
#data = obj.findInMountainArray(array = [1,2,3,4,5,3,1], target = 3)
data = obj.findInMountainArray(array = [0,1,2,4,2,1], target = 3)
print(data)