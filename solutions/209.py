# Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target, nums):
        length = len(nums)
        Invalid = length + 1
        left, right = 0, 0

        added = nums[left]
        if added >= target:
            return 1

        ans = Invalid
        while True:
            if left + 1 <= right and added - nums[left] >= target:
                added -= nums[left]
                left += 1
                ans = min(ans, right - left + 1)
                continue

            if right < length - 1:
                added += nums[right + 1]
                right += 1
                if added >= target:
                    ans = min(ans, right - left + 1)
                continue

            # cannot reduct left side, cannot expand to right.
            # break here
            break

        return 0 if ans == Invalid else ans

if __name__ == "__main__":
    sol = Solution()
    target = 7
    nums = [2,3,1,2,4,3]

    target = 4
    nums = [1,4,4]

    target = 11
    nums = [1,1,1,1,1,1,1,1]

    target = 11
    nums = [12]

    target = 15
    nums = [1,2,3,4,5]

    print(sol.minSubArrayLen(target, nums))
