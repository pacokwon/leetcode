# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        uniqCount = 0
        index = 0
        length = len(nums)
        while index < length:
            first = nums[index]

            index += 1
            while index < length and first == nums[index]:
                index += 1

            nums[uniqCount] = first
            uniqCount += 1

        return uniqCount

if __name__ == "__main__":
    sol = Solution()
    inp = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(inp))
    print(inp)
