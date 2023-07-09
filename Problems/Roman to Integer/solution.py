import io
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_def = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev_ord = 0
        integer = 0
        for i in s[::-1]:
            if prev_ord == 0 :
                integer = roman_def.get(i,0)
                prev_ord = roman_def.get(i,0)
                continue
            if roman_def.get(i,0) >= prev_ord:
                integer += roman_def.get(i,0)
            else :
                integer -= roman_def.get(i,0)
            prev_ord = roman_def.get(i,0)
                
        return integer

obj = Solution()
#data = obj.romanToInt(s = "III")
#data = obj.romanToInt(s = "LVIII")
data = obj.romanToInt(s = "MCMXCIV")
print(data)