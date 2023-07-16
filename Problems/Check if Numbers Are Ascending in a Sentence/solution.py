import io
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x = 0
        for i in s.split(' '):
            if not i.isnumeric():
                continue
            if int(i) <= x :
                return False
            x = int(i)
        return True

obj = Solution()
#data = obj.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles")
data = obj.areNumbersAscending(s = "hello world 5 x 5")
print(data)