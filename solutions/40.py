# Combination Sum II

class Solution:
    def group(self, nums):
        nums.sort()
        index = 0
        length = len(nums)
        grouped = []
        while index < length:
            val = nums[index]
            count = 0
            while index < length and val == nums[index]:
                count += 1
                index += 1
            grouped.append((val, count))
        return grouped

    def combinationSum2(self, candidates, target):
        grouped = self.group(candidates)
        length = len(grouped)

        def helper(index, added, path, ans):
            if added == target:
                ans.append(path)
                return

            if index == length:
                return

            num, count = grouped[index]
            for c in range(count + 1):
                if added + num * c > target:
                    break

                helper(index + 1, added + num * c, path + [num] * c, ans)

        ans = []
        helper(0, 0, [], ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,5,2,1,2]
    target = 0
    print(sol.combinationSum2(candidates, target))
