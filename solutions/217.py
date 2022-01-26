# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        index = 0
        length = len(nums)
        while index < length - 1:
            if nums[index] == nums[index + 1]:
                return True

            index += 1

        return False

if __name__ == "__main__":
    sol = Solution()
    inp = [1, 2, 1, 4]
    print(sol.containsDuplicate(inp))
