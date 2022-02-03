# Divide a String Into Groups of Size k

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        ans = [s[i*k:i*k+k] for i in range(length // k)]
        if length % k == 0:
            return ans

        last = length // k * k
        left = length - last
        padding = k - left
        ans.append(s[last:last+left] + fill * padding)
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "abcdefghi"
    k = 2
    fill = "x"
    print( sol.divideString(s, k, fill) )
