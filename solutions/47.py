# Permutations II

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
            grouped.append([val, count])
        return grouped

    def permuteUnique(self, nums):
        length = len(nums)
        grouped = self.group(nums)
        path = [None] * length

        def helper(count, grouped, path, ans):
            if count == length:
                ans.append(list(path))
                return

            for i in range(len(grouped)):
                if grouped[i][1] != 0:
                    path[count] = grouped[i][0]
                    grouped[i][1] -= 1
                    helper(count + 1, grouped, path, ans)
                    grouped[i][1] += 1

        ans = []
        helper(0, grouped, path, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.permuteUnique(nums))
