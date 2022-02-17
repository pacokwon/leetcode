from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        mostOneDel = arr[0]
        noDel = arr[0]
        ans = arr[0]

        for n in arr[1:]:
            mostOneDel = max(noDel, mostOneDel + n, n)
            noDel = max(noDel + n, n)
            ans = max(mostOneDel, ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1,-2,0,3]
    arr = [1,-2,-2,3]
    arr = [-1,-1,-1,-1]
    print(sol.maximumSum(arr))
