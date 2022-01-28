# Arithmetic Slice
# realized that O(n) is possible after looking at the solutions, but this solution is O(n²)

class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        if length < 3:
            return 0

        Invalid = -1
        dp = [[Invalid] * length for _ in range(length)]
        ans = 0

        def sliceDiff(arr, start, end):
            diff = arr[start] - arr[start + 1]
            idx = start + 1
            while idx + 1 < end:
                if diff != arr[idx] - arr[idx + 1]:
                    return Invalid
                idx += 1

            return -diff if diff < 0 else diff

        # window of size 3 to length
        window = 3
        # initialize dp
        index = 0
        while index <= length - window:
            dp[index][index + window - 1] = sliceDiff(nums, index, index + window)
            if dp[index][index + window - 1] >= 0:
                ans += 1
            index += 1

        window = 4
        while window <= length:
            index = 0
            while index <= length - window:
                start, end = index, index + window - 1
                first = dp[start][end - 1]
                second = dp[start + 1][end]

                if first == Invalid or second == Invalid:
                    index += 1
                    continue

                if first == second:
                    dp[start][end] = first
                    ans += 1
                else:
                    dp[start][end] = Invalid

                index += 1

            window += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,8,4,5]
    print(sol.numberOfArithmeticSlices(nums))
