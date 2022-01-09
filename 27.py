# Remove Element

class Solution:
    def removeElement(self, nums, val):
        # list to keep an index of values to KEEP
        indices = [index for index, n in enumerate(nums) if n != val]
        length = len(indices)
        index = 0
        while index < length:
            nums[index] = nums[indices[index]]
            index += 1

        return length

if __name__ == "__main__":
    sol = Solution()
    inp = [0,1,2,2,3,0,4,2]
    print(sol.removeElement(inp, 2))
    print(inp)
