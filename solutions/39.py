# Combination Sum

class Solution:
    def combinationSum(self, candidates, target):
        length = len(candidates)
        def helper(index, added, path, ans):
            if added == target:
                ans.append(path)
                return

            if index == length:
                return

            num = candidates[index]

            count = 0
            tmpAdded = added
            while tmpAdded <= target:
                helper(index + 1, tmpAdded, path + [num] * count, ans)
                count += 1
                tmpAdded += num

        ans = []
        helper(0, 0, [], ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    candidates = [8]
    target = 1
    print(sol.combinationSum(candidates, target))
