# 3Sum
class Solution:
    def threeSum(self, nums):
        nums.sort()

        ans = []
        length = len(nums)
        i = 0
        while i < length:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = length - 1
            target = -nums[i]

            while j < k:
                twosum = nums[j] + nums[k]
                if twosum > target:
                    k -= 1
                elif twosum < target:
                    j += 1
                else:
                    # found it!
                    ans.append([nums[i], nums[j], nums[k]])

                    # skip through duplicate values
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    # this is what actually changes the value of nums[j], nums[k]
                    j += 1
                    k -= 1

            i += 1

        return ans

# [-4, -1, -1, 0, 1, 2]
#  0   1   2   3  4  5

if __name__ == "__main__":
    sol = Solution()
    inp = [-1,0,1,2,-1,-4]
    print(sol.threeSum(inp))
