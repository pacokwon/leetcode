# Optimal Division
class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"

        lhs = nums[0]
        rhs = '/'.join(str(e) for e in nums[1:])
        return f"{lhs}/({rhs})"

if __name__ == "__main__":
    sol = Solution()
    inp = [2]
    print(sol.optimalDivision(inp))
