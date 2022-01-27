# Permutations

class Solution:
    def permute(self, nums):
        length = len(nums)
        visited = [False] * length

        ans = []
        def helper(choices, count, visited, ans):
            if count == length:
                ans.append(list(choices))
                return

            for index, v in enumerate(visited):
                if not v:
                    visited[index] = True
                    choices[count] = nums[index]
                    helper(choices, count + 1, visited, ans)
                    visited[index] = False

        helper([None] * length, 0, visited, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    inp = [0]
    print(sol.permute(inp))
