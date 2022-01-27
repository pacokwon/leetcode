# Combinations

class Solution:
    def combine(self, n, k):
        ans = []

        def helper(choices, start, count, ans):
            if count == k:
                # cloning the list here
                ans.append(list(choices))
                return

            for i in range(start, n + 1):
                choices[count] = i
                helper(choices, i + 1, count + 1, ans)

        helper([None] * k, 1, 0, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 1
    k = 1
    print(sol.combine(n, k))
