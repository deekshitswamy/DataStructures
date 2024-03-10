import io
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = list()

        n1_ptr = n2_ptr = 0
        while n1_ptr < len(nums1) and n2_ptr < len(nums2):
            if nums1[n1_ptr] < nums2[n2_ptr]:
                n1_ptr += 1

            elif nums1[n1_ptr] > nums2[n2_ptr]:
                n2_ptr += 1

            else:
                if nums1[n1_ptr] not in result:
                    result.append(nums1[n1_ptr])

                n1_ptr += 1
                n2_ptr += 1
        
        return result

obj = Solution()
#data = obj.intersection(n = 1)
#data = obj.intersection(n = 2)
data = obj.intersection(n = 2)
print(data)