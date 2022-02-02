# Find All Possible Recipes from Given Supplies
"""
toughest part was to handle cycles,
which I assumed wouldn't exist in the test cases but did
"""

from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        0 not computed yet
        -1 computing
        1 Possible
        2 Impossible
        """
        possible = [0] * len(recipes)
        sp = set(supplies)
        ans = []

        def check(index):
            nonlocal ans, sp, possible

            if possible[index] > 0:
                return possible[index]

            if possible[index] == -1:
                possible[index] = 2
                return 2

            # computing
            possible[index] = -1
            p = True
            for ing in ingredients[index]:
                if ing not in sp:
                    try:
                        idx = recipes.index(ing)
                    except ValueError:
                        idx = -1

                    if idx == -1:
                        p = False
                        break

                    if check(idx) == 2:
                        p = False
                        break

            if p:
                ans.append(recipes[index])
                sp.add(recipes[index])

            possible[index] = 1 if p else 2
            return possible[index]

        for index in range(len(possible)):
            check(index)

        return ans

if __name__ == "__main__":
    sol = Solution()
    recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
    ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
    supplies = ["f","hveml","cpivl","d"]
    print(sol.findAllRecipes(recipes, ingredients, supplies))
