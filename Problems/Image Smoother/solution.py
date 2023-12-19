import io
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        img_np = np.zeros((m+2, n+2), dtype=np.int32)
        img_np[1:-1, 1:-1] = img
        cnt_np = np.zeros((m+2, n+2), dtype=np.int32)
        cnt_np[1:-1, 1:-1] = 1

        reduce_img = lambda x: sum([x[o1:m+o1, o2:n+o2] for o1, o2 in product(range(3), range(3))])


        ans = reduce_img(img_np) // reduce_img(cnt_np)
        return ans.tolist()

obj = Solution()
#data = obj.imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]])
data = obj.imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]])
print(data)