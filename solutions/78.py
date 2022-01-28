# Subsets

class Solution:
    def subsets(self, nums):
        length = len(nums)
        path = [None] * length

        def helper(start, count, path, ans):
            if start == length:
                ans.append(path[:count])
                return

            helper(start + 1, count, path, ans)

            path[count] = nums[start]
            helper(start + 1, count + 1, path, ans)

        ans = []
        helper(0, 0, path, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [0]
    print(sol.subsets(nums))
