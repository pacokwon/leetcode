# Removing Minimum Number of Magic Beans

from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # insight 1: the number of beans only decrease
        # insight 2: we can choose a bag, and adjust other bags to have the same number as the chosen bag, or make it 0
        beans.sort()
        length = len(beans)

        return sum(beans) -  max(b * (length - index) for index, b in enumerate(beans))

if __name__ == "__main__":
    sol = Solution()
    beans = [4,1,6,5]
    beans = [2,10,3,2]
    print(sol.minimumRemoval(beans))
