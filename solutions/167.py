# Two Sum II

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            added = numbers[left] + numbers[right]
            if added == target:
                return [left + 1, right + 1]

            if added > target:
                right -= 1
            else:
                left += 1

        return []


if __name__ == "__main__":
    sol = Solution()
    numbers = [5,25,75]
    target = 100
    print(sol.twoSum(numbers, target))
