# Valid Mountain Array

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False

        n = len(arr)
        index = 1
        while index < n and arr[index - 1] < arr[index]:
            index += 1

        # if no decreasing or increasing point
        if index == 1 or index == n:
            return False

        while index < n:
            if arr[index - 1] > arr[index]:
                index += 1
            else:
                return False

        return True

if __name__ == "__main__":
    sol = Solution()
    arr = [2,1]
    arr = [3,5,5]
    arr = [0,3,3,1]
    arr = [9,8,7,6,5]
    print(sol.validMountainArray(arr))
