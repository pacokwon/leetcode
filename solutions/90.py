# Subsets II

class Solution:
    def group(self, nums):
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

    def subsetsWithDup(self, nums):
        nums.sort()
        grouped = self.group(nums)
        length = len(grouped)

        def helper(index, count, path, ans):
            if index == length:
                ans.append(path)
                return

            val, count = grouped[index]
            for c in range(count + 1):
                helper(index + 1, count + c, path + [val] * c, ans)

        ans = []
        helper(0, 0, [], ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.subsetsWithDup(nums))
