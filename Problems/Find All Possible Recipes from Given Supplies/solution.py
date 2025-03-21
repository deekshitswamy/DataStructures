import io
from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        pass

obj = Solution()
#data = obj.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"])
#data = obj.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"])
data = obj.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"])
print(data)