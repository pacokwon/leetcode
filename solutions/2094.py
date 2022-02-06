# Finding 3-Digit Even Numbers
# belongs between easy and medium... in my opinion

from typing import List

class Solution:
    def group(self, nums: List[int]) -> List[List[int]]:
        index = 0
        length = len(nums)
        ans = []
        while index < length:
            val = nums[index]
            count = 0
            while index < length and val == nums[index]:
                count += 1
                index += 1
            ans.append([val, count])
        return ans

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        grouped = self.group(digits)
        length = 3
        ans = []
        def comb(count, acc, ans):
            if count == length:
                ans.append(acc)
                return

            for g in grouped:
                v, c = g
                if c == 0: continue
                # no leading zeroes allowed
                if count == 0 and v == 0:
                    continue

                # no odd numbers allowed at end
                if count == length - 1 and v % 2 == 1:
                    continue

                g[1] -= 1
                comb(count + 1, acc * 10 + v, ans)
                g[1] += 1

        comb(0, 0, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    digits = [2,2,8,8,2]
    digits = [2,1,3,0]
    print( sol.findEvenNumbers(digits) )
