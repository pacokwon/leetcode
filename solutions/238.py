# Product of Array Except Self

# tripped a lot on this problem..should have thought through
class Solution:
    def productExceptSelf(self, nums):
        product = 0
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            if product == 0:
                product = num
            else:
                product *= num

        if zeroCount == 1:
            return [product if num == 0 else 0 for num in nums]
        elif zeroCount > 1:
            return [0] * len(nums)

        return [product // num for num in nums]

if __name__ == "__main__":
    sol = Solution()
    inp = [0, 4, 1]
    print(sol.productExceptSelf(inp))
